import socket
import os
import sys
import traceback
from threading import Thread
from pwn import *

PORT = int(os.environ.get("PORT", 6703))


def thread_func(conn, ip, port):
    r = process('./sneak_to_roof')
    o = r.recvline()
    conn.sendall(o)
    c = conn.recv(256)
    print(c)
    if(sys.getsizeof(c) >  256):
        conn.sendall(b'Too long input\n')
    else:
        r.sendline(c)
        try:
            o = r.recv()
            conn.sendall(o)
        except:
            conn.sendall(b'Error occured processing yout input')
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
