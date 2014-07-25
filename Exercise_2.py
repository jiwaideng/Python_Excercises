def near(n):
	uitkomst = ""

	if n >= 90 and n <= 110:
		uitkomst = True, abs(100 - n) 
	
	elif n >= 190 and n <= 210:
		uitkomst = True, abs(200 - n)

	elif n < 90:
		uitkomst = False, 100 - n

	elif n > 110 and n < 190:
		uitkomst = False, 200 - n

	else:
		uitkomst = False, abs(200 - n) 
	
	print(uitkomst)
	return(uitkomst)

near(89)
near(103)
near(195)
near(223)
near(64)