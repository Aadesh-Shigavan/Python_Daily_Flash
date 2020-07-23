'''Program 5: Write a Program that accepts Two integers from user and prints
maximum number from them.'''

num1, num2 = [int(i) for i in input("Input : ").split()]
if(num1 > num2):
    print("Max : ", num1)
elif(num1 == num2):
    print("Equal")
else:
    print("Max : ", num2)
