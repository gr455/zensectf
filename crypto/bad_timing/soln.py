from Crypto.Cipher import AES
import base64
import time
from hashlib import md5

enc = '3Y6SUOJw4QCM1fukxt2TWB2eO5giteB2TjzxJudeb2mnQYqLoND2bzU14Fc4hKZGi6Ezmeyh7MeHQT21GwCSDouhM5nsoezHh0E9tRsAkg4='

cipher = base64.b64decode(enc)

#Change the range max value according to the day of the event you are solving this challenge.
#I'm assuming that you are doing it on 20th
for tim in range(int(time.time())-(86400*2), (int(time.time()))):
    key = md5(str(tim)).digest()
    aes = AES.new(key, AES.MODE_ECB)
    plaintext = aes.decrypt(cipher)
    print(plaintext)
