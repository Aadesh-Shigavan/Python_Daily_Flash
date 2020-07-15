unit = int(input("Enter Unit : "))

if unit >= 0 and unit <= 50 :
	print(unit * 0.50,"Charges")
elif unit >= 50 and unit <= 150:
	print(unit * 0.75,"Charges")
elif unit >= 150 and unit <= 250:
	print(unit * 1.20,"Charges")
elif unit > 250 :
	print(unit * 1.50,"Charges")