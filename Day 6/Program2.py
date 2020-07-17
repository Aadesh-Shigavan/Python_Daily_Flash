a = int(input("Enter a number : "))

b = 0

for i in range(1,a+1):
	b = i + b
print("The sum of number up to",a,": ",b)