''' Program 2: Write a Program to Print following Pattern
1
2 3
4 5 6
7 8 9 10 '''

num = 1

for i in range(4):
	for j in range(i + 1):
		print(num,end=" ")
		num+=1
	print()
	 

