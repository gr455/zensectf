import socket
import os
import sys
import traceback
import random
import time
from threading import Thread
from pwn import *

PORT = int(os.environ.get("PORT", 6717))


def thread_func(conn, ip, port):
    r = process('./sneak_to_roof')
    o = r.recvline()
    conn.sendall(o)
    print(o)
    o = r.recvline()
    conn.sendall(o)
    print(o)
    count = 0
    c = conn.recv(1024)
    l = c.splitlines()
    if(len(c) == 2):
        r.sendline(l[0])
        o = r.recvline()
        conn.sendall(o)
        r.sendline(l[1])
        output = r.recv()
        conn.sendall(output)
    else
        conn.sendall(b'Couldnt process output\n')
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
