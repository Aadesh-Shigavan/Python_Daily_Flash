''' Program 2: Write a Program that accepts Two integers from user and prints the
series of factorial of all numbers between those two inputs. ''' 

num1, num2 = [int(i) for i in input("Input : ").split()]
for i in range(num1, num2 + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j 
    print("Fact of ", i, " = ", fact) 
	

