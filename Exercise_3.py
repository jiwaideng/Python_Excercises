def missing(a, b):
	hoera = ""
	count = 0
	for i in a:
		if b == count:
			jefke = ""
		else:
			hoera = hoera + i
		count = count + 1
	
	print(hoera)

missing("water", 3)
missing("hello", 1)
missing("jantje", 5)


	
"""
water = a[0]+a[1]+a[2]+a[3]+a[4]
watr = a[0]+a[1]+a[2]+a[4]
0 = w
1 = a
2 = t
3 = e
4 = r
"""	