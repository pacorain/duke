from logging import Handler
from http.client import HTTPSConnection
import json


class DiscordLoggingHandler(Handler):
    def __init__(self, webhooks: list, *args, **kwargs):
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

    def emit(self, record):
        message = self.format(record)
        url = self.urls[record.levelno]
        body = json.dumps({"content": message})
        headers = {'Content-Type': 'application/json'}
        con = HTTPSConnection('discordapp.com')
        con.request('POST', url, body, headers)
        # Tell the server we're done with the request
        test = con.getresponse()
        con.close()
