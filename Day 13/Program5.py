''' Program 5: Write a Program that accepts Three integers from user and prints
minimum number from them. '''

num1 = int(input("num1 : "))

num2 = int(input("num2 : "))

num3 = int(input("num3 : "))

if num1 < num2 and num1 < num3:
	print("The minimum number among ",num1,num2,"&",num3,"is",num1)
elif num2 < num1 and num2 <num3:
	print("The minimum number among ",num1,num2,"&",num3,"is",num2)
else:
	print("The minimum number among ",num1,num2,"&",num3,"is",num3)