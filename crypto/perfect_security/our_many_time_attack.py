#!/usr/bin/env python 
import string
import collections
import sets

# XORs two string
def strxor(a, b):     # xor two strings (trims the longer input)
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

# 10 unknown ciphertexts (in hex format), all encrpyted with the same key
'''c1 = "315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e"
c2 = "234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f"
c3 = "32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb"
c4 = "32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa"
c5 = "3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070"
c6 = "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4"
c7 = "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce"
c8 = "315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3"
c9 = "271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027"
c10 = "466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83"
ciphers = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
# The target ciphertext we want to crack
target_cipher = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"
'''
c_flag = "2e0d0700452a27661c5f1d1e38101a5e593d554e02130d"
c1 = "0707491c4e0c53440616490f47470116001111411354150c520e061100000800414c0f01120606454d13"
c2 = "1c0d4900411e53540f0e1d4e1348114f530706520454501c1d41070d454f134e491a001c1411481d1406"
c3 = "00000c1d00011600140e1e4e0f45530b0005005441441148140d1202000008004409061c1e041c495b5c"
c4 = "151b490a4f1c534b09001e42474d150b4e071653414903481e0818000008144156051117495a4641585e"
c5 = "1d481c00450d5354084f1d060e4e1f4f540a0454414d09481e08150000180753000d451a15150f45504b"
c6 = "1911491e4f1d1b45154f080210410d1c0016004c0d5350051741070a001c0b494c09450f091048504146"
c7 = "1d481d1b4f1c1448134f001a4757151c00050a490f47501c1d41110a540703520001004247161d54145b"
c8 = "03000c1d00101c55470d1b070947540245420a55150c500b130f531c4f1a46494e18170103010b45145f"
c9 = "03000807000d1c001e001c4e0045004f570a004e41591f1d5202010a531c4641000100001315044c4d12"
c10 = "00000c5357060153134f190f1554540046420d4117491e0f52005308450112414c4c0c020b1a0d534712"
c11 = "111e0c01590b1c441e4f001d47410309550e45540945030d5205121c5341466954e281b5164e021a0755535a"
c12 = "12071b534d1053570f00050b474c1d09454e45694144190c1ce281b807454b0109570005034e2e540d56515c"
c13 = "1c091f1600101c55471c0c0b090003074116454915e280b903481e0818000000135400180d0b151144007947"
ciphers = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13]
target_cipher = "2e0d0700452a27661c5f1d1e38101a5e593d554e02130d"

'''c_flag = "2e0d0700452a27661c0159194759441a00090b10160007000b414311504f5715005c0b5d4743594d074f"
c1 = "0707491c4e0c53440616490f47470116001111411354150c520e061100000800414c0f01120606454d13"
c2 = "1c0d4900411e53540f0e1d4e1348114f530706520454501c1d41070d454f134e491a001c1411481d1406"
c3 = "00000c1d00011600140e1e4e0f45530b0005005441441148140d1202000008004409061c1e041c495b5c"
c4 = "151b490a4f1c534b09001e42474d150b4e071653414903481e0818000008144156051117495a4641585e"
c5 = "1d481c00450d5354084f1d060e4e1f4f540a0454414d09481e08150000180753000d451a15150f45504b"
c6 = "1911491e4f1d1b45154f080210410d1c0016004c0d5350051741070a001c0b494c09450f091048504146"
c7 = "1d481d1b4f1c1448134f001a4757151c00050a490f47501c1d41110a540703520001004247161d54145b"
c8 = "03000c1d00101c55470d1b070947540245420a55150c500b130f531c4f1a46494e18170103010b45145f"
c9 = "03000807000d1c001e001c4e0045004f570a004e41591f1d5202010a531c4641000100001315044c4d12"
c10 = "00000c5357060153134f190f1554540046420d4117491e0f52005308450112414c4c0c020b1a0d534712"
c11 = "111e0c01590b1c441e4f001d47410309550e45540945030d5205121c5341466954e281b5164e021a0755535a"
c12 = "12071b534d1053570f00050b474c1d09454e45694144190c1ce281b807454b0109570005034e2e540d56515c"
c13 = "1c091f1600101c55471c0c0b090003074116454915e280b903481e0818000000135400180d0b151144007947"
ciphers = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
target_cipher = "2e0d0700452a27661c0159194759441a00090b10160007000b414311504f5715005c0b5d4743594d074f"
'''
# To store the final key
final_key = [None]*150
# To store the positions we know are broken
known_key_positions = set()

# For each ciphertext
for current_index, ciphertext in enumerate(ciphers):

	counter = collections.Counter()
	# for each other ciphertext
	for index, ciphertext2 in enumerate(ciphers):
		if current_index != index: # don't xor a ciphertext with itself
			for indexOfChar, char in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))): # Xor the two ciphertexts
				# If a character in the xored result is a alphanumeric character, it means there was probably a space character in one of the plaintexts (we don't know which one)
				if char in string.printable and char.isalpha(): counter[indexOfChar] += 1 # Increment the counter at this index
	knownSpaceIndexes = []

	# Loop through all positions where a space character was possible in the current_index cipher
	for ind, val in counter.items():
		# If a space was found at least 7 times at this index out of the 9 possible XORS, then the space character was likely from the current_index cipher!
		if val >= 7: knownSpaceIndexes.append(ind)
	#print knownSpaceIndexes # Shows all the positions where we now know the key!

	# Now Xor the current_index with spaces, and at the knownSpaceIndexes positions we get the key back!
	xor_with_spaces = strxor(ciphertext.decode('hex'),' '*150)
	for index in knownSpaceIndexes:
		# Store the key's value at the correct position
		final_key[index] = xor_with_spaces[index].encode('hex')
		# Record that we known the key at this position
		known_key_positions.add(index)

# Construct a hex key from the currently known key, adding in '00' hex chars where we do not know (to make a complete hex string)
final_key_hex = ''.join([val if val is not None else '00' for val in final_key])
# Xor the currently known key with the target cipher
output = strxor(target_cipher.decode('hex'),final_key_hex.decode('hex'))
# Print the output, printing a * if that character is not known yet
print ''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])

'''
Manual step
'''
# From the output this prints, we can manually complete the target plaintext from:
# The secuet-mes*age*is: Wh** usi|g **str*am cipher, nev***use th* k*y *ore than onc*
# to:
# The secret message is: When using a stream cipher, never use the key more than once

# We then confirm this is correct by producing the key from this, and decrpyting all the other messages to ensure they make grammatical sense
'''target_plaintext = "The secret message is: When using a stream cipher, never use the key more than once"
key = strxor(target_cipher.decode('hex'),target_plaintext)
print target_plaintext
#print "The below is"
#print key.decode('hex')
for cipher in ciphers:
	print strxor(cipher.decode('hex'),key)'''
