
year = int(input("Enter the year"))

if year%4==0:
    if year%100==0 and year%400!=0:
        print("is not leap year")
    else:
        print("is leap year")
else:
    print("is not leap year")