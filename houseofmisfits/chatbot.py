import os
import requests


class Chatbot:
    def __init__(self):
        self.run_nr = 0
        self.send_initial_message()

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

        Currently does nothing.
        :return:
        """
        self.run_nr += 1
        if self.run_nr >= 5:
            raise Exception("This program has a loop that doesn't do anything. Exiting.")
