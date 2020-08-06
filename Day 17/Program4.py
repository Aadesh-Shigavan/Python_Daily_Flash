''' Program 4: Write a Program to Print following Pattern.

+ = + =
+ = +
+ = 
+ 		'''


for i in range(0,4):
	for j in range(0,4):
		if i + j > 3:
			print(" ",end=" ")
		elif j % 2 == 0:
			print("+",end=" ")
		else:
			print("=",end=" ")
	print()