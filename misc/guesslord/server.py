#!/usr/bin/env python3

import socket
import os
import sys
import traceback
import random
import time
from threading import Thread

PORT = int(os.environ.get("PORT", 6969))
flag = open('flag.txt', 'r').readline()

def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 4096):
    RANDOM_NUMBER = random.randint(0, 1000000)
    tries = 0
    conn.sendall(b"I'm am guessing a number between 0 and 1000000\n")
    conn.sendall(b"You have 5 seconds and 30 tries to guess it correctly :)\n")
    max_time = 5
    start = time.time()

    while True:
        input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)

        siz = sys.getsizeof(input_from_client_bytes)
        if  siz >= MAX_BUFFER_SIZE:
            print("The length of input is probably too long: {}".format(siz))

        try:
            guess = int(input_from_client_bytes.decode("utf8").rstrip())
        except ValueError:
            conn.sendall(b"That's not an int!\n")
            break
        else:
            tries += 1
            if guess < RANDOM_NUMBER:
                conn.sendall(f"Your guess is lesser than actual number; {40 - tries} tries left\n".encode())
            elif guess > RANDOM_NUMBER:
                conn.sendall(f"Your guess is greater than the actual number; {40 - tries} tries left\n".encode())
            else:
                conn.sendall(f"\n Congratulations! Here is the flag\n{flag}\n".encode())
                break

        if time.time()-start > max_time: 
           conn.sendall(f"\nTime Limit Exceeded !!!!\n".encode()) 
           break

        if tries > 30:
            conn.sendall(f"\n No. of tries Exceeded \n")
            break

    conn.sendall(b"Bye! \n")
    conn.close()
    print('Connection ' + ip + ':' + port + " ended")

def start_server():

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')

    try:
        soc.bind(("0.0.0.0", PORT))
        print('Socket bind complete')
    except socket.error as msg:
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    soc.listen(10)
    print('Socket now listening')

    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Accepting connection from ' + ip + ':' + port)
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print("Terible error!")
            traceback.print_exc()
    soc.close()

start_server()  