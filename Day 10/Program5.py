''' Program 5: Write a Program that accepts an integer from user and prints all of
its perfect divisors.'''

num = int(input("Input : "))

for i in range(1,num):
	if num % i == 0:
		print(i,end=" ")
print()
