import hashlib 

reader = open('being_a_boy.txt', 'r').read()            #Read from the book text file

lst = reader.replace("\n", " ").split(" ")              
lst[:] = (value for value in lst if value != '')
lst[:] = (x.lower() for x in lst)                       #All this is formatting basically, removing punctuations,converting to lowercase, etc. Don't want to explain it all, it is better to understand each                                                         function used for oneself
s = 'b754015b1f05de447a0915eea5238c1f3310a4826b3190d5b7fe4739bc3bc992'
for i in lst:
    word = "zenseCTF{"+i+"}"                             #Wrapping around
    hashval = hashlib.sha256(word.encode()).hexdigest()  
    if hashval == s:                                     #Checking equality
        print(word)
