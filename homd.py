#!/usr/bin/env python
import sys
import time
import logging

from houseofmisfits import Chatbot, MessageScheduler

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)


def run():
    try:
        logger.info("House of Misfits Webhooks Daemon started.")
        chat_bot = Chatbot()
        while True:
            chat_bot.eval()
            time.sleep(1)
    except:
        logger.critical("Something happened and the webhooks daemon is shutting down.\n", exc_info=True)


def debug():
    logger.info("Simulating new week in debugging branch.")
    MessageScheduler.simulate_week()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if 'run' == sys.argv[1]:
            run()
        elif 'debug' == sys.argv[1]:
            debug()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: {} run|debug".format(sys.argv[0]))
        sys.exit(2)
