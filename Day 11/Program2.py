''' Program 2: Write a Program which accepts two integers from user and swaps
their insertion order.
Input : 20 30
Output :
Before Swap : 20 30
After Swap : 30 20 '''

num1,num2 = input().split()

print("Before swap : ",num1,num2)

num3,num4 = num2,num1

print("After swap : ",num3,num4)