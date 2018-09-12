def emod(a, b, p):
	if b == 0:
		return 1
	elif b % 2 == 0:
		c = b/2
		d = emod(a, c, p)
		print('d: ', d, 'expo: ', c, 'Return: ', d*d % p)
		return d*d % p
	else:
		c = b-1
		k = emod(a, c, p);
		print('k: ', k, 'expo: ', c, 'Return: ', a % p * k % p)
		return ((a % p) * k) % p

emod(2, 100, (int)(1e9+7))