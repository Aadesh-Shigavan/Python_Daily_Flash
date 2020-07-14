marks = input("Enter the marks phy chem bio math comp in string fromat").split()

percent = eval("(float(marks[0])+float(marks[1])+float(marks[2])+float(marks[3])+float(marks[4]))/500*100")#500 marks overall  100 each paper

if percent>=90:
    print("Grade A")
elif percent>=80:
    print("Grade B")
elif percent>=70:
    print("Grade C")
elif percent>=60:
    print("Grade D")
elif percent>=40:
    print("Grade E")
elif percent < 40:
    print("Grade F")