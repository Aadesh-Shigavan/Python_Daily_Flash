''' Program 3: Write a Program to Print following Pattern.
A A A A A 
B B B B 
C C C 
D D 
E
'''

a = 64

for i in range(1,6):
	a+=1
	for j in range(1,6):
		if i + j >= 7:
			print(" ",end=" ")
		else:
			print(chr(a),end=" ")
	print()