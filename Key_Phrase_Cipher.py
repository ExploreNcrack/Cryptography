def Key_Phrase_Cipher(secret_word,raw_string):
	plaintext = ''
	c = 0
	for s in raw_string:
		if ord('a')<=ord(s)<=ord('z'):
			if ord(s) >= ord(secret_word[c%len(secret_word)].lower()):
				plaintext += chr( ord('a') + (ord(s)-ord(secret_word[c%len(secret_word)].lower())) )
			else:
				plaintext += chr( ord('a') + ord('z') - ord(secret_word[c%len(secret_word)].lower())+ (ord(s)-ord('a'))+1 )
			c+=1
		elif ord('A')<=ord(s)<=ord('Z'):
			if ord(s) >= ord(secret_word[c%len(secret_word)].upper()):
				plaintext += chr( ord('A') + (ord(s)-ord(secret_word[c%len(secret_word)].upper())) )
			else:
				plaintext += chr( ord('A') + ord('Z') - ord(secret_word[c%len(secret_word)].upper())+ (ord(s)-ord('A')) +1 )
			c+=1
		else:
			plaintext += s
	return plaintext


def Key_Phrase_Encode(secret_word,raw_string):
	ciphertext = ''
	i=0
	for s in raw_string:
		if ord('a')<=ord(s)<=ord('z'):
			ciphertext += chr(ord('a')+(ord(secret_word[i%len(secret_word)].lower())-ord('a')+(ord(s)-ord('a')))%26)
			i+=1
		elif ord('A')<=ord(s)<=ord('Z'):
			ciphertext += chr(ord('A')+(ord(secret_word[i%len(secret_word)].lower())-ord('a')+(ord(s)-ord('A')))%26)
			i+=1
		else:
			ciphertext += s

	return ciphertext


print(Key_Phrase_Encode('HAMHAMH','STUDENT STUDENT'))
print(Key_Phrase_Cipher('discrete','Jzwck nhf! Bwm jrzx idzfgu jnpo ustbw.'))