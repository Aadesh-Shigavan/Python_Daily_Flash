''' Program 1: Write a Program which detects whether the entered number is
perfect or not . '''

num = int(input("Enter a number : "))

total = 0

for i in range(1,num):
	if num % i == 0:
		total+=i 
if total == num:
	print(total," is perfect number")
else:
	print(total," is not perfect number")