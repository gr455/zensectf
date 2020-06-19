#!usr/bin/python

#from secret import flag
from Crypto.Cipher import AES
from hashlib import md5
import time


for i in range(int(time.time() - 10*86400) , int(time.time() + 10*86400)): #pow(10,8),pow(10,10)):
    key = md5(str(i).encode('utf-8')).digest() #int(time.time()+(86400*5)))).digest()
    aes = AES.new(key, AES.MODE_ECB)
    for padding in range(0,17):
        #padding = 16 - len(flag) % 16
        outData = aes.encrypt(flag + padding* str(padding))
        if(outData.encode('base64')) == '3Y6SUOJw4QCM1fukxt2TWB2eO5giteB2TjzxJudeb2mnQYqLoND2bzU14Fc4hKZGi6Ezmeyh7MeHQT21GwCSDouhM5nsoezHh0E9tRsAkg4=':
            print( (key,padding))


