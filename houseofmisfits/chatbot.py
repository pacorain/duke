import os
import requests

from houseofmisfits import MessageScheduler


class Chatbot:
    def __init__(self):
        self.send_initial_message()
        self.scheduler = MessageScheduler()
        self.scheduler.refresh()

    def send_initial_message(self):
        """
        Send a test message to demonstrate that the server is working.
        """
        webhook_url = os.getenv('SYS_WEBHOOK_URL')
        message = "Webhook successfully started on " + os.name

        payload = {"content": message}

        req = requests.post(webhook_url, json=payload, headers={'Content-Type': 'application/json'})
        print(req.content)

    def eval(self):
        """
        Check for any pending actions and perform them.
        """
        self.scheduler.run_pending()

