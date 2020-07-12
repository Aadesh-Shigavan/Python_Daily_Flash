month = {'1':'Janaury is a 31 days month','2':'Februry is a 29 (Leap) days month','3':'March is a 31 days month','4':'April is a 30 days month','5':'May is a 31 days month','6':'June is a 30 days month','7':'July is a 31 days month','8':'August is a 31 days month','9':'September is a 30 days month','10':'October is a 31 days month','11':'November is a 30 days month','12':'December is a 31 days month'}

a = input("Enter a Number : ")

if a >= '1' or a <= '12' :
	print(month.get(a))
else :
	print("Enter a Valid Number !")