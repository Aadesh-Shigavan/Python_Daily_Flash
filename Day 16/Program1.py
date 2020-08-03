''' Program 1: Write a Program to that prints the series which increases with the
number entered by user. '''

a = int(input("Input : "))

b = 1

for i in range(1,11):
	b+=a
	print(b,end=" ")
print()