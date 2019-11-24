FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN ["python", "setup.py", "build"]
RUN ["python", "setup.py", "install"]
RUN ["python", "setup.py", "test"]

ENTRYPOINT ["python", "hom.py"]
CMD "run"