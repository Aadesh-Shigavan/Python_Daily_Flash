'''Program 4: Write a Program to simulate simple calculator. Accept two integers
from user and sign of operation to perform '''

a = int(input("Enter First Number : "))

b = int(input("Enter Second Number : "))

sign = input("Enter Sign of Operation : ")

if sign == '+':
	print("Addition of ",a,"&",b,"is",a + b)
elif sign == '-':
	print("Subtraction of ",a,"&",b,"is",a - b)
elif sign == '*':
	print("Multiplication of ",a,"&",b,"is",a * b)
elif sign == '-':
	print("Division of ",a,"&",b,"is",a / b)
else :
	print("Enter Valid Operatio..!")