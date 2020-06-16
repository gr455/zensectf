import socket
import os
import sys
import traceback
import random
import time
import subprocess
from threading import Thread
#from pwn import *

PORT = int(os.environ.get("PORT", 6711))


def thread_func(conn, ip, port, MAX_BUFFER_SIZE = 1024):
    incoming = conn.recv(MAX_BUFFER_SIZE)
    data, temp = os.pipe()
    print(type(incoming))
    if(sys.getsizeof(incoming) >  MAX_BUFFER_SIZE):
        print("Exceeded buffer limit")
    else:
        if(type(incoming) == bytes):
            os.write(temp,incoming);
        else:
            os.write(temp,bytes(incoming,"utf-8"));
        print(temp)
        print(incoming)
        os.close(temp)
        output = subprocess.check_output("./movie_screening",stdin = data,shell = True)
        print(output)
        conn.sendall(output)
    conn.close()
    print('Connection '+ip+':'+port+" ended")

def receiver():
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
            Thread(target=thread_func, args=(conn, ip, port)).start()
        except:
            print("Connections exceeded retry in a while...\n")
            traceback.print_exc()
    soc.close()

receiver()
