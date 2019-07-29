import os
from datetime import date, timedelta, datetime

import json

from houseofmisfits import Message


class MessageScheduler:
    def __init__(self):
        self.messages = []
        self.date = date.today() - timedelta(days=1)
        self.rules = MessageScheduler.load_rules()

    def run_pending(self):
        for message in self.messages:
            if datetime.now() >= message.scheduled_time:
                message.send()
                self.messages.remove(message)

    @staticmethod
    def load_rules():
        rules = {}
        rules_dir = os.getenv('WORKSPACE') + '/rules'
        for file in os.listdir(rules_dir):
            with open(rules_dir + '/' + file, 'r') as json_file:
                rule = json.load(json_file)
                rules.update(rule)
        return rules

    def refresh(self):
        # TODO: Move this to a config file
        # Schedule a ping every five minutes
        for message_time in (datetime.now() + timedelta(minutes=n) for n in range(0, 1440, 5)):
            message = Message('aspen_general', '#wellness_reminder#', self.rules, message_time)
            self.messages.append(message)
