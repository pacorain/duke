import time

from houseofmisfits import Chatbot


def run():
    chatbot = Chatbot()
    while True:
        chatbot.eval()
        time.sleep(1)


if __name__ == '__main__':
    run()
