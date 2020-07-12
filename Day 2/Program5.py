a,b,c = input("Input : ").split()

total = int (a) + int (b) + int (c)
print(total)

if total == 180:
	print("Triangle is Valid")
else:
	print("Triangle is not a Valid")