def difference(n):
	if n <= 20:
		difference = 20 - n
	else:
		difference = (n - 20) * 2

	return difference 

print(difference(19))
print(difference(10))
print(difference(23))
