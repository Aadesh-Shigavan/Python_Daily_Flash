a,b,c = input("Input : ").split()

if a > b and a > c :
	print(a,"is Max among", a ,b ,"&", c)
if  b > a and b > c :
	print(b,"is Max among", a ,b ,"&", c)
else :
	print(c,"is Max among", a ,b ,"&", c)