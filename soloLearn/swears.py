swears = ("duck", "shoot", "poopie")
def censor(phrase):

	check = ""
	if check == phrase:										#checks if phrase is empty
		return "The phrase is empty."
	else:
		sentence = phrase
		for swear in swears:								#traverses swears
			if swear in sentence:							#checks phrase for swear
				censored = "***"
				sentence = sentence.replace(swear, censored)


		return sentence

x = input('Enter phrase: ')
print(censor(x))