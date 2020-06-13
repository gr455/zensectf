import socket
import os
import sys
import traceback
import random
import time
from threading import Thread
from pwn import *

PORT = int(os.environ.get("PORT", 6711))


def thread_func(conn, ip, port, MAX_BUFFER_SIZE = 1024):
    incoming = conn.recv(MAX_BUFFER_SIZE)
    r = process('./screening')
    r.sendline(incoming)
    output = r.recv()
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
