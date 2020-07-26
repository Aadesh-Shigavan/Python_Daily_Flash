''' Program 1: Write a Program to print series of Even numbers ranging between
two numbers entered by user. '''

a = int(input("Min no of series : "))

b = int(input("Min no of series : "))

for i in range(a,b+1):
	if i % 2 == 0:
		print(i,end=" ")
print()