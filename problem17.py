#calculation of percentage of marks in three subs:

total_marks=int(input("enter the total marks in each sub: "))


marks1=int(input("enter the marks in first sub: ")) 
if(marks1>total_marks):
    print("invalid") 
else:
    perc1=(marks1/total_marks)*100
    print("the precentage of marks in subject 1 is: ", perc1)

marks2=int(input("enter the marks in second sub: "))
if (marks2>total_marks):
    print("invalid")
else:
    perc2=(marks2/total_marks)*100
    print("the precentage of marks in subject 2 is: ", perc2)


marks3=int(input("enter the marks in third sub: "))
if(marks3>total_marks):
    print("invalid")
else:
    perc3=(marks3/total_marks)*100
    print("the precentage of marks in subject 3 is: ", perc3)






