''' Program 1: Write a Program to Print following Pattern
1
2 2
3 3 3
4 4 4 4 '''

n = 1

for i in range(4):
	for j in range(4):
		if i >= j:
			print(n ,end=" ")
		else:
			print( )
	n+=1
print()