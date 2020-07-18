''' Program 4: Write a Program that accepts an integer from user and print table
of that number.'''

tableof = int(input("Enter a Number : "))

for num in range(1,11):
	print(tableof * num,end =" ")
print()
