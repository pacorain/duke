FROM python:3

WORKDIR /usr/src/app

RUN sudo echo "America/New_York" > /etc/timezone
RUN sudo dpkg-reconfigure -f noninteractive tzdata

COPY . .
RUN ["python", "setup.py", "build"]
RUN ["python", "setup.py", "install"]
RUN ["python", "setup.py", "test"]

ENTRYPOINT ["python", "hom.py"]
CMD "run"