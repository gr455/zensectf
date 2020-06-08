import math
from gmpy2 import mpz
from Crypto.Util.number import inverse

def gcd(x,y):
    if y <= x:
        return gcd(y,x)
    if y%x == 0:
        return x
    return gcd( y%x,x)

def extended_euclid(x,y):
    if( y<= x):
        return extended_euclid(y,x)
    if gcd(x,y) != 1:
        return -1
    r = [y,x]
    q = [] #int(y/x)]
    a = [0,1]
    while r[-1] != 1:
        q.append(int(r[-2]/r[-1]))
        r.append(r[-2]%r[-1])
        a.append( (a[-2] - q[-1]*a[-1])%y)
    return a[-1]

# Python program to compute 
# factorial of big numbers 

# Maximum number of digits in 
# output 
MAX=100000

# This function multiplies x 
# with the number represented by res[]. 
# res_size is size of res[] or 
# number of digits in the number 
# represented by res[]. This function 
# uses simple school mathematics 
# for multiplication. 
# This function may value of res_size 
# and returns the new value of res_size 
def multiply(x, res, res_size): 

	# Initialize carry 
	carry = 0

	# One by one multiply n with 
	# individual digits of res[] 
	for i in range(res_size): 
		prod = res[i] * x + carry 

		# Store last digit of 
		# 'prod' in res[] 
		res[i] = prod % 10

		# Put rest in carry 
		carry = prod // 10

	# Put carry in res and 
	# increase result size 
	while (carry): 
		res[res_size] = carry % 10
		carry = carry // 10
		res_size+=1

	return res_size 


# This function finds 
# power of a number x 
def power(x,n): 
	
	# printing value "1" for power = 0 
	if (n == 0) : 
            print("1") 
	return
	
	res=[0 for i in range(MAX)] 
	res_size = 0
	temp = x 

	# Initialize result 
	while (temp != 0): 
		res[res_size] = temp % 10; 
		res_size+=1
		temp = temp // 10


	# Multiply x n times 
	# (x^n = x*x*x....n times) 
	for i in range(2, n + 1): 
		res_size = multiply(x, res, res_size) 

	print(x , "^" , n , " = ",end="") 
	for i in range(res_size - 1, -1, -1): 
		print(res[i], end="") 

# Driver program 

exponent = 100
base = 2
power(base, exponent) 

# This code is contributed 
# by Anant Agarwal. 




def convert_to_message(s):

    d = {}
    d2 = {}

    for i in range(ord('a'), ord('z')+1):
        d[chr(i)] = i-ord('a')+1
    #d['_'] = ord('_') - ord('a') + 1
    s2 = ""
    for i in s:
        print(d[i])
        s2 += str(d[i])
    return int(s2)


def convert_to_message(s):

    d = {}
    d2 = {}

    for i in range(ord('a'), ord('z')+1):
        d[chr(i)] = i-ord('a')+1
    #d['_'] = ord('_') - ord('a') + 1
    s2 = ""
    for i in s:
        print(d[i])
        s2 += str(d[i])
    return int(s2)


def convert_to_number(n):
    s2 = ""


p = 982451653
q = 961748927
n = p*q 
e = 65537

phi = (p-1)*(q-1)

d = inverse(e,phi) #extended_euclid(e,phi)

#msg = convert_to_message("weakrsaisawesome") 

c = 9430007809292879
print(f' d {d} c {c}')
msg = pow(c,d,n)

print(msg)
'''print(f'n : {n}')
print(f'e : {e}')
print(f'ciphertext : {ciphertext}')

'''
