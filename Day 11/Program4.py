''' Program 4: Write a Program to Print following Pattern.
a
A A
a a a
A A A A
a a a a a '''

for i in range(1,6):
	if i % 2 == 1:
		print("a " * i)
	else :
		print("A " * i)