Age = int(input("Enter age : "))

sex = input("Enter Sex : ")

marital_status = input("Enter Status : ")

if sex == 'F':
	print("Employee will work only in urban area")
elif sex == 'M'and Age >= 20 and Age <= 40:
	print("Employee can work anywhere")
elif sex == 'M' and Age >= 40 and Age <= 60:
	print("Employee will work in urban area only")
else :
	print("ERROR !")