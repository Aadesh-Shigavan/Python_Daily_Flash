''' Program 2: Write a Program to all the numbers ranging between 1 to 100 that
# are divisible by 4 and 7. '''

for i in range(1,101):
	if i % 4 == 0 and i % 7 == 0:
		print(i,end=" ")
print()