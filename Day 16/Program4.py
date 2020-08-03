''' Program 4: Write a Program to Print following Pattern.
7
6 5
5 4 3
4 3 2 1 '''



num = 7

for itr in range(4):
    num = 7 -itr
    for jtr in range(itr+1):
        print(num,end=" ")
        num = num - 1
    print(" ") 