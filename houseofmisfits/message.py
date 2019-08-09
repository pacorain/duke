import datetime
import os
import requests
import yaml
import tracery
from tracery.modifiers import base_english
import logging
logger = logging.getLogger(__name__)

logging.getLogger("requests").setLevel(logging.WARNING)


class Message:
    def __init__(self, webhook_name: str, message: str, rules: dict, scheduled_time: datetime.datetime):
        """
        Initialize a message
        :param webhook_name: The name of the webhook to use
        :param message: The tracery root of the message to send
        :param scheduled_time: What time the message is scheduled for
        """
        self.webhook_name = webhook_name
        self.rules = rules
        self.message = self.flatten(message)
        self.scheduled_time = scheduled_time
        logger.debug("Message scheduled for {}".format(self.scheduled_time.isoformat()))
        self.is_sent = False

    def flatten(self, message):
        """
        Calles the tracery "flatten" function to generate a human-friendly message
        :return: the flattened message
        """
        grammar = tracery.Grammar(self.rules)
        grammar.add_modifiers(base_english)
        flattened_message = grammar.flatten(message)
        logger.debug("'{}' flattened to '{}'".format(message, flattened_message))
        return flattened_message

    def send(self):
        """
        Sends the message to the Discord webhook
        """
        if self.is_sent:
            raise Message.AlreadySentException()
        webhook_url = self._get_webhook_url()
        payload = {"content": self.message}
        headers = {'Content-Type': 'application/json'}
        req = requests.post(webhook_url, json=payload, headers=headers)
        self.is_sent = True
        logger.debug("Message sent to {} with status code {}. Response: {}".format(
            self.webhook_name, req.status_code, req.content))

    def describe(self):
        return "`{}` - `{}`\n{}".format(self.scheduled_time.isoformat(), self.webhook_name, self.message)

    def _get_webhook_url(self):
        """
        Gets the appropriate Discord webhook URL from webhooks.yaml
        """
        webhooks_path = os.getenv('WORKSPACE') + '/webhooks.yml'
        with open(webhooks_path, 'r') as webhooks_file:
            all_webhooks = yaml.safe_load(webhooks_file)
        webhook = all_webhooks[self.webhook_name]
        logger.debug('Loaded webhook {} successfully'.format(self.webhook_name))
        return webhook

    class AlreadySentException(Exception):
        pass

