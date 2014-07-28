def missing(word, index):
	new_word = ""
	if index == 0:
		new_word = word[1:]
	else:
		new_word = new_word + word[0:index]
		new_word = new_word + word[index+1:len(word)]
	return new_word

def missing2(word, index):
	new_word = ""
	count = 0
	for i in word:
		if count == index:
			count = count + 1
			continue
		new_word = new_word + i
		count = count + 1
	return new_word

def missing3(word, index):
	new_word = ""
	count = 0
	for i in word:
		if count == index:
			count = count + 1
		else:
			new_word = new_word + i
			count = count + 1
	return new_word

def missing4(word, index):
	new_word = ""
	count = 0
	while count < len(word):
		if count == index:
			count = count + 1
		else:
			new_word = new_word + word[count]
			count = count + 1
	return new_word

print(missing("Jordy", 2))
print(missing2("Jordy", 2))
print(missing3("Jordy", 2))
print(missing4("Jordy", 2))
