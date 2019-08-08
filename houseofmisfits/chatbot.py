from houseofmisfits import MessageScheduler
import logging

logger = logging.getLogger(__name__)

class Chatbot:
    def __init__(self):
        logger.debug("Initializing webhooks bot")
        self.scheduler = MessageScheduler()
        self.scheduler.refresh()

    def eval(self):
        """
        Check for any pending actions and perform them.
        """
        self.scheduler.run_pending()

