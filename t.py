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


print(find_multiplicative_inverse(26,3))