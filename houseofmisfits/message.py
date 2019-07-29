import datetime
import requests
import json

import tracery
from tracery.modifiers import base_english


class Message:
    def __init__(self, webhook_name: str, message: str, rules: dict, scheduled_time: datetime):
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
        self.is_sent = False

    def flatten(self, message):
        """
        Calles the tracery "flatten" function to generate a human-friendly message
        :return: the flattened message
        """
        grammar = tracery.Grammar(self.rules)
        grammar.add_modifiers(base_english)
        return grammar.flatten(message)

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
        print(req.content)
        self.is_sent = True

    def _get_webhook_url(self):
        """
        Gets the appropriate Discord webhook URL from webhooks.json
        """
        with open('webhooks.json', 'r') as webhooks_file:
            all_webhooks = json.load(webhooks_file)
        return all_webhooks[self.webhook_name]

    class AlreadySentException(Exception):
        pass

