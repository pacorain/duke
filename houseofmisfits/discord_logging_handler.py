from logging import Handler
import logging
from http.client import HTTPSConnection
import json


class DiscordLoggingHandler(Handler):
    def __init__(self, webhooks: list, mention_id=None, mention_level=logging.CRITICAL, *args, **kwargs):
        super(DiscordLoggingHandler, self).__init__(*args, **kwargs)
        if isinstance(webhooks, str):
            webhooks = [webhooks] * 5
        self.urls = {}
        for i in range(5):
            if i > len(webhooks) - 1:
                webhooks[i] = webhooks[i - 1]
            log_level = (i + 1) * 10
            server_url = '/' + '/'.join(webhooks[i].split('/')[3:])
            self.urls.update({
                log_level: server_url
            })
        self.mention_id = mention_id
        self.mention_level = mention_level

    def setMention(self, mention_id, mention_level=None):
        self.mention_id = mention_id
        if mention_level is not None:
            self.mention_level = mention_level

    def emit(self, record):
        message = self.format(record)
        if record.levelno >= self.mention_level and self.mention_level is not None:
            message = "<@&{0}> {1}".format(self.mention_id, message)
        url = self.urls[record.levelno]
        body = json.dumps({"content": message})
        headers = {'Content-Type': 'application/json'}
        con = HTTPSConnection('discordapp.com')
        con.request('POST', url, body, headers)
        # Tell the server we're done with the request
        con.getresponse()
        con.close()
