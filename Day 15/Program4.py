''' Program 4: Write a Program to Print following Pattern.
7
7 6
6 5 4
4 3 2 1'''

a = 7

for i in range(1,5):
	for j in range(i):
		a -=1
		print(a+i,end=" ")

	print()
