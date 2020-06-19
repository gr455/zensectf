'''
620031587
Net-Centric Computing Assignment
Part A - RSA Encryption
'''
import math
import random
from Crypto.Util.number import inverse 

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q,e):
    '''if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    '''
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    '''e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)'''
    
    #Use Extended Euclid's Algorithm to generate the private key
    d = inverse(e,phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key,n) for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(pow(char,key,n)) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
    

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    
    #p = 913306253407263289162829739833884164120826498520494179889201
    #q = 952335717381953830472884308915455070778381159122901477263083
    #e = 65537
    #n = p*q
    #if( gcd(e,p*q) != 1):
    #    print("Completely false")
    print "RSA Encrypter/ Decrypter"
    p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
    q = int(raw_input("Enter another prime number (Not one you entered above): "))
    e = int(raw_input("Enter e"))
    n = p*q
    print "Generating your public/private keypairs now . . ."
    public, private = generate_keypair(p, q,e)
    print "Your public key is ", public ," and your private key is ", private
    #message = raw_input("Enter a message to encrypt with your private key: ")
    #encrypted_msg = encrypt(public, message)
    #print "Your encrypted message is: "
    #print encrypted_msg
    #print ''.join(map(lambda x: str(x), encrypted_msg))
    encrypted_msg = input() #[int(x) for x in str(input())]
    #for i in encrypted 
    print type(encrypted_msg)
    print "Decrypting message with public key ", public ," . . ."
    print "Your message is:"
    print decrypt(private, encrypted_msg)
