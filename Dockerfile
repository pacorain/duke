FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN ["python", "setup.py", "build"]
RUN ["python", "setup.py", "install"]

RUN echo ${WEBHOOKS_FILE}
COPY ${WEBHOOKS_FILE} webhooks.yml
RUN ["ls", "webhooks.yml"]

ENTRYPOINT ["python", "hom.py"]
CMD "run"