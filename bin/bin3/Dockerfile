FROM python:3.8

ENV PWNLIB_NOTERM=true

RUN pip3 install pwntools

WORKDIR /usr/src/app
COPY . .

ENTRYPOINT python3 server2.py
