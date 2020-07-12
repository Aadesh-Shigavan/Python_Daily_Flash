WeekDays = { '0' : 'Monday', '1' : 'Tuesday', '2': 'Wednesday', '3' :'Thursday','4':'Friday','5':'Saturday','6':'Sunday'}

number = input("Enter a number : ")

if number >= '0' and number <= '6' :
	print(WeekDays.get(number))
else :
	print("Enter a Valid Number")