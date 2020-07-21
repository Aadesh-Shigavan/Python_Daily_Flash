''' Program 4: Write a Program to Print following Pattern.

0
1 1
0 0 0
1 1 1 1
0 0 0 0 0 '''




for itr in range(5):
    for outr in range(0,itr+1):
        print("0",end=" ") if itr%2==0 else print("1",end = " ")
    print(" ")