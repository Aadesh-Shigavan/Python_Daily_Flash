'''Program 3: Write a program that accepts two integers from user and prints
addition of their Cubes and subtraction of their Squares. '''

a,b = input("Enter Numbers : ").split()

a_cube = int (a) * int (a) * int(a)

b_cube = int(b) * int(b) * int(b)

print("Addition of ",a_cube,"&",b_cube,"is ",int (a_cube) + int (b_cube))

a_square = int (a) * int (a)

b_square = int(b) * int(b) 

print("Subtraction of ",a_square,"&",b_square,"is ",int (a_square) - int (b_square))