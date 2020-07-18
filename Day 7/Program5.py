''' Program 5 : Write a Program to print following Pattern.
Output :
0
0 0
0 0 0
0 0 0 0


for i in range(4):
	for j in range(4):
		if i < j :
			print("")
		else:
			print("0",end=" ")
print()
'''

'''

for out in range(4):
    for inner in range(out+1):
        print("0",end=" ")
    print(" ")  

    '''

for i in range(4):
    print("0 "*(i + 1))