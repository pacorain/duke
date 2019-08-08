from houseofmisfits import MessageScheduler
import logging

logger = logging.getLogger(__name__)

class Chatbot:
    def __init__(self):
        logger.debug("Initializing webhooks bot")
        self.scheduler = MessageScheduler()
        self.scheduler.refresh()
        self.i = 0

    def eval(self):
        """
        Check for any pending actions and perform them.
        """
        self.scheduler.run_pending()
        self.i += 1
        if self.i >= 15:
            raise OSError("Example error: this is what happens when a wrench gets thrown into things.")

