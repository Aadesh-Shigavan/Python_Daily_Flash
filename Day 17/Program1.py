''' Program 1: Write a Program to that prints series of odd numbers in reverse
order from the limiting number entered by user '''

num = int(input("Enter a Number : "))

for i in range(1,num+1):
	if num % 2 == 1:
		print(num,end=" ")
		num-=1
	else:
		num-=1
print()