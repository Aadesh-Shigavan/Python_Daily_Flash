''' Program 3: Write a Program to print Cubes and Squares of all Odd numbers
ranges between given input number. '''

num = int(input("Input : "))

cube = 0

square = 0

for i in range(1,num+1):

	cube = i * i * i

	square = i * i

	if i % 2 == 1:
		print("Cube of",i,"is : ",cube,"Square of",i,"is : ",square)

