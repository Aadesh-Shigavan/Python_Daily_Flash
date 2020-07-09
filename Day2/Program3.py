a = input("Enter Something : ")

if a >= 'a' or a <= 'z' and a >= 'A' or a >= 'Z':
	print(a,"is a Alphabet")
elif ord(a) >= 48 and ord(a) <= 57 :
	print(a,"is a digit")
elif  ord(a) >= 33 and ord(a) <= 47 :
	print(a,"is a Special character")
else :
	print("other")