''' Program 1: Write a Program to print all the numbers ranging between 1 to 100
that are divisible by 3 or 5. '''

for i in range(1,101):
	if i % 3 == 0 or i % 5 == 0:
		print(i,end=" ")
print()