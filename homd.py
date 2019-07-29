#!/usr/bin/env python
import os
import sys
import time
import logging
from daemon import Daemon
from houseofmisfits import Chatbot

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(os.getenv('WORKSPACE') + '/homd.log')
logger.addHandler(handler)


class HouseOfMisfitsDaemon(Daemon):
    def run(self):
        logger.info("Starting chatbot.")
        chatbot = Chatbot()
        while True:
            try:
                chatbot.eval()
                time.sleep(1)
            except Exception as e:
                logger.critical("Something happened, closing.")
                logger.critical(e)


if __name__ == "__main__":
    daemon = HouseOfMisfitsDaemon('/tmp/homd.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: {} start|stop|restart".format(sys.argv[0]))
        sys.exit(2)
