''' Program 4: Write a Program to Print following Pattern.
1
4  9
16 25 36
49 64 81 100 '''

a = 1

for i in range(4):
	for j in range(4):
		if j <= i :
			print(a * a,end=" ")
			a+=1
	print()
