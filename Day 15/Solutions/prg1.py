a,b = input().split()
c=int(a)
d = int(b)


print("before swap: a =",a,"&","b =",b)


if c > d:
	difference = c-d
	c -=difference
	d+=difference
	print("after swap: a =",c,"&","b =",d)
else:
	difference = d -c
	c+=difference
	d-=difference
	print("after swap: a =",c,"&","b =",d)