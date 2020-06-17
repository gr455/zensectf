import socket
import os
import sys
import traceback
import subprocess
from threading import Thread

PORT = int(os.environ.get("PORT", 6711))


def thread_func(conn, ip, port, MAX_BUFFER_SIZE = 201):
    conn.sendall(b'Please enter you name\n')
    incoming = conn.recv(MAX_BUFFER_SIZE)
    data, temp = os.pipe()
    print(sys.getsizeof(incoming))
    if(sys.getsizeof(incoming) >  MAX_BUFFER_SIZE):
        conn.sendall(b'Exceeded buffer limit')
    else:
        if(type(incoming) == bytes):
            os.write(temp,incoming);
        else:
            os.write(temp,bytes(incoming,"utf-8"));
        os.close(temp)
        output = subprocess.check_output("./movie_screening",stdin = data,shell = True)
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
