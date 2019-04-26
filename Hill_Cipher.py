'''
1.Plaintext is split up into n letter blocks
2.If the number of plaintext letters is not a multiple of n, add xx
in n=2 case 
plaintext "Pizza" is split up into "Pi zz ax".
Given a,b,c,d in mod 26 and a block "x y" in the plaintext
E(x) = a*x+b*y (mod 26)
E(y) = c*x+d*y (mod 26)

D(x) = delta*d*x  - delta*b*y (mod26)
D(y) = delta*-c*x + delta*a*y (mod26) 
'''


def Find_delta_in_2by2_matrix(a,b,c,d):
	return 1/(a*d-b*c)


def Hill_Cipher_Decode(a,b,c,d,raw_string):
	plaintext = ''
	delta = Find_delta_in_2by2_matrix(a,b,c,d)
	for i in range(0,len(raw_string),2):
		if ord('a')<=ord(s)<=ord('z'):
			x =  (delta*d*(ord(raw_string[i])-ord('')) - delta*b*raw_string[i+1])%26
			y = -delta*c*raw_string[i] + delta*a*raw_string[i+1]
			plaintext+= 
		elif ord('A')<=ord(s)<=ord('Z'):


		else:
			plaintext+=s

	return plaintext


def Hill_Cipher_Encode():
	pass


def main():

	pass


if __name__ == '__main__':
	main()




	
