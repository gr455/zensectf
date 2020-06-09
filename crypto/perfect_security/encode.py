def strxor(a, b):     # xor two strings (trims the longer input)
    #a = hex(a)
    #b = hex(b)
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

flag = "zenseCTF{0tp_0n1y_0nc3}" #n0w y0u kn0w 0tp 15 0n3 71m3}"
print(len(flag))
key = "This is going to be a phrase of  length 42"
print(len(key))
p1 = "So one day a guy started out on a journey!"
p2 = "He saw that the secret to the universe = 42"
p3 = "Then he saw he'd get da flag on decryption"
p4 = "As you know, madness is like gravity...all it takes is a little push."
p5 = "I used to think that my life was a tragedy, but now I realize, it’s a comedy."
p6 = "My mother always tells me to smile and put on a happy face. She told me I had a purpose: to bring laughter and joy to the world."
p7 = "I thought it was going to bother me, but it really hasn’t."
p8 = "When you bring me out, can you introduce me as Joker?"
p9 = "What do you get when you cross a mentally ill loner with a society abandons him and treats him like trash?"
p10 = "The worst part of having a mental illness is people expect you to behave as if you don’t."
p11 = "Everybody is awful these days. It’s enough to make anyone crazy. If it was me dying on the sidewalk, you’d walk right over me. I pass you everyday and you don’t notice me!"
p12 = "For my whole life, I didn’t know if I even really existed. But I do, and people are starting to notice."
p13 = "Have you seen what it’s like out there, Murray? Everybody just yells and screams at each other. Nobody’s civil anymore! Nobody thinks what it’s like to be the other guy."

print(len(p7))
l = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]
def encrypt(a,b):
    return strxor(a,b).encode('utf-8').hex()

def encrypt_list(c):
    l = []
    for i in c:
        l.append(encrypt(i,key))
    return l


c_flag = (strxor(flag,key)).encode('utf-8').hex()
print(f'c_flag = "{c_flag}"')
c = encrypt_list(l)
for i in range(len(c)):
    print(f'c{i+1} = "{c[i]}"')
print(f'ciphers = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13]')
print(f'target_cipher = "{c_flag}"')
print(c)
'''c1 = (strxor(p1,key)).encode('utf-8').hex()
c2 = (strxor(p2,key)).encode('utf-8').hex()
c3 = (strxor(p3,key)).encode('utf-8').hex()
c4 = encrypt(p4,key)


print(f'c1 = {c1}')
print(f'c2 = {c2}')
print(f'c3 = {c3}')'''
