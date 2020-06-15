FROM python:3.8

RUN pip3 install pycryptodome

WORKDIR /usr/src/app
COPY . .

CMD [ "python3", "server.py" ]