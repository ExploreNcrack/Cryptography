def find_multiplicative_inverse(mod_num,n):
	t = mod_num
	for i in range(mod_num):
		t+=mod_num
		if (t+1)%n == 0:
			t=(t+1)//n
			while t>mod_num:
				t-=mod_num
			return t

	return -1


def Linear_Code_Decipher(k,a,raw_string):
	plain_text = ''
	a_inverse = find_multiplicative_inverse(26,a)
	for s in raw_string:
		if ord('a')<=ord(s)<=ord('z'):
			plain_text += chr( ord('a') + (a_inverse*(ord(s)-ord('a')-k))%26 )
		elif ord('A')<=ord(s)<=ord('Z'):
			plain_text += chr( ord('A') + (a_inverse*(ord(s)-ord('A')-k))%26 )
		else:
			plain_text+=s
	return plain_text



raw = input('Enter Linear code: ')
print(Linear_Code_Decipher(6,3,raw))