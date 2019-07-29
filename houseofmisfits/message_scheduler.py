import os
from datetime import date, timedelta, datetime, time

import json
import logging
from pytz import timezone

from houseofmisfits import Message

logger = logging.getLogger(__name__)


weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}


class MessageScheduler:
    def __init__(self):
        self.messages = []
        self.date = date.today()
        self.rules = MessageScheduler.load_rules()

    def run_pending(self):
        tz = timezone('US/Eastern')
        if date.today() > self.date:
            self.refresh()
            self.date = date.today()
        for message in self.messages:
            if datetime.now(tz=tz) >= message.scheduled_time:
                logger.debug("Sending message with {}: {}".format(message.webhook_name, message.message))
                message.send()
                self.messages.remove(message)

    def refresh(self):
        for scheduled_message in MessageScheduler.load_schedules():
            schedule_type = scheduled_message['schedule']['type']
            if schedule_type == 'hourly':
                self.schedule_hourly(scheduled_message)
            elif schedule_type == 'weekly':
                self.schedule_weekly(scheduled_message)
            else:
                raise KeyError(schedule_type)
        self.date = date.today()

    def schedule_hourly(self, message):
        tz = timezone('US/Eastern')
        start_time = datetime.combine(date.today(), time(0, 0, 0), tzinfo=tz)
        interval = message['schedule']['interval']
        webhook = message['webhook']
        unflat_text = message['message']
        for message_time in (start_time + timedelta(hours=n) for n in range(0, 24, interval)):
            if datetime.now(tz=tz) > message_time:
                continue
            new_message = Message(webhook, unflat_text, self.rules, message_time)
            self.messages.append(new_message)

    def schedule_weekly(self, message):
        tz = timezone('US/Eastern')
        day_of_week = weekdays[date.today().weekday()]
        webhook = message['webhook']
        unflat_text = message['message']
        if day_of_week in message['schedule']['days']:
            dt = date.today()
            h, m = message['schedule']['time'].split(':')
            tm = time(int(h), int(m))
            message_time = datetime.combine(dt, tm, tzinfo=tz)
            if datetime.now(tz=tz) > message_time + timedelta(minutes=15):
                # Don't schedule the message -- it's already too late
                return
            new_message = Message(webhook, unflat_text, self.rules, message_time)
            self.messages.append(new_message)

    @staticmethod
    def load_rules():
        rules = {}
        rules_dir = os.getenv('WORKSPACE') + '/rules'
        for file in os.listdir(rules_dir):
            with open(rules_dir + '/' + file, 'r') as json_file:
                rule = json.load(json_file)
                rules.update(rule)
        return rules

    @staticmethod
    def load_schedules():
        schedules = []
        schedules_dir = os.getenv('WORKSPACE') + '/schedules'
        for file in os.listdir(schedules_dir):
            with open(schedules_dir + '/' + file, 'r') as json_file:
                schedule = json.load(json_file)
                schedules += schedule
        return schedules
