#!/usr/bin/env python
import sys
import time
import logging

from daemon import Daemon
from houseofmisfits import Chatbot, MessageScheduler

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)


class HouseOfMisfitsDaemon(Daemon):
    def run(self):
        try:
            logger.info("House of Misfits Webhooks Daemon started.")
            chatbot = Chatbot()
            while True:
                chatbot.eval()
                time.sleep(1)
        except:
            logger.critical("Something happened and the webhooks daemon is shutting down.\n", exc_info=True)

    @staticmethod
    def debug():
        logger.info("Simulating new week in debugging branch.")
        MessageScheduler.simulate_week()


if __name__ == "__main__":
    daemon = HouseOfMisfitsDaemon('/tmp/homd.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'fg' == sys.argv[1]:
            daemon.run()
        elif 'debug' == sys.argv[1]:
            HouseOfMisfitsDaemon.debug()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: {} start|stop|restart".format(sys.argv[0]))
        sys.exit(2)
