def Caesar_Decipher(raw_string,k):
	plain_text = ''
	for s in raw_string:
		if ord('a')<=ord(s)<=ord('z'):
			#lower case
			plain_text += chr(ord('a')+(ord(s)-ord('a')+k)%26)
		elif ord('A')<=ord(s)<=ord('Z'):
		    #upper case
			plain_text += chr(ord('A')+(ord(s)-ord('A')+k)%26)
		else:
			plain_text+=s
	return plain_text



raw=input("Please enter a encrypted Caesar code: ")
print(Caesar_Decipher(raw,22)) 