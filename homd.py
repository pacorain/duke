#!/usr/bin/env python
import os
import sys
import time
import logging

import yaml

from daemon import Daemon
from houseofmisfits import Chatbot, DiscordLoggingHandler


class HouseOfMisfitsDaemon(Daemon):
    def run(self):
        logger = HouseOfMisfitsDaemon.configure_discord_logging()
        try:
            logger.info("House of Misfits Webhooks Daemon started.")
            chatbot = Chatbot()
            while True:
                chatbot.eval()
                time.sleep(1)
        except:
            logger.critical("Something happened and the webhooks daemon is shutting down.\n", exc_info=True)

    @staticmethod
    def configure_discord_logging():
        logger = logging.getLogger()
        # TODO: Set logging level dynamically
        logger.setLevel(logging.DEBUG)
        critical_url = os.getenv('SYS_WEBHOOK_URL')
        workspace_dir = os.getenv('WORKSPACE')
        with open(workspace_dir + '/webhooks.yml', 'r') as webhooks_file:
            wh = yaml.safe_load(webhooks_file)
        urls = [
            wh['logging_debug'],
            wh['logging_info'],
            wh['logging_warning'],
            wh['logging_error'],
            critical_url
        ]
        h = DiscordLoggingHandler(urls)
        h.setMention(wh['logging_mention_roleid'], logging.ERROR)
        logger.addHandler(h)
        return logger


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
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: {} start|stop|restart".format(sys.argv[0]))
        sys.exit(2)
