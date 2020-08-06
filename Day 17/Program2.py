''' Program 2: Write a Program to that prints series of Even numbers in reverse
order from the limiting number entered by user. '''

num = int(input("Enter a Number : "))

for i in range(1,num+1):
	if num % 2 == 0:
		print(num,end=" ")
		num-=1
	else:
		num-=1
print()