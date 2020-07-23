''' Program 3: Write a Program to print Cubes and Squares of all Even numbers
ranges between given input number. '''

a = int(input("input : "))



for i in range(a+1):
	if i % 2 == 0:

		cube = i * i * i

		square = i * i

		print("Cube of ",i,":",cube,"and Square of",i,":",square)