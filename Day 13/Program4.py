''' Program 4: Write a Program to Print following Pattern. 
1
8  27
64 125 216
343 512 729 1000 '''

a = 1

for i in range(1,5):
	for j in range(1,5):
		if j <= i:
			print(a * a * a,end=" ")
			a+=1
	print()