''' Program 1: Write a Program to print series of odd numbers ranging between
two numbers entered by user. '''

Min_of_Series = int(input("Min of series : "))

Max_of_Series = int(input("Max of series : "))

for i in range(Min_of_Series,Max_of_Series):
	if i % 2 == 1:
		print(i,end=" ")