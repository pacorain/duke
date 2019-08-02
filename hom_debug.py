import logging
import os
import time

from houseofmisfits import Chatbot


def run():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(os.getenv('WORKSPACE') + '/homd.log')
    logger.addHandler(handler)
    chatbot = Chatbot()

    while True:
        chatbot.eval()
        time.sleep(1)


if __name__ == '__main__':
    run()
