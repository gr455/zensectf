FROM python:3.6


RUN pip install flask
RUN pip install pyjwt==1.7.0
RUN pip install pycrypto ecdsa
RUN pip install cryptography

RUN rm /usr/local/lib/python3.6/site-packages/jwt/algorithms.py
COPY algorithms.py /usr/local/lib/python3.6/site-packages/jwt/algorithms.py
COPY pyth /app
WORKDIR /app

ENTRYPOINT python3 main.py