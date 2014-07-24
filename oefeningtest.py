"""
gegeven zijn een string a en een integer b

test:

a="hello", b=2 ==> output: "hel"
a="jiwai", b=1 ==> output: "ji"
a="noob", b=3 ==> output: "noob"

ar = ["hello", "jiwai", "noob", "aap"]
woord = "link"
woord[1] 
ar[0][2]
ar[1]

"""

def deelwoord(a, b):
	uitkomst = ""
	for i in range(b+1):
		uitkomst = uitkomst + a[i]
	print(uitkomst)

deelwoord("hello", 2)
deelwoord("jiwai", 1)
deelwoord("noob", 3)

