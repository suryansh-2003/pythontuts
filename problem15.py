#Let a list with name of 4 employees working in a company be created.


name1=input("Enter ther name of the first employee: ")
name2=input("Enter ther name of the second employee: ")
name3=input("Enter ther name of the third employee: ")
name4=input("Enter ther name of the fourth employee: ")

employees=[name1, name2, name3, name4]
print(employees)

#If we suppose that employee 3 left the company and a new employee joined in his/her place:-->
#updating the list:

employees[2]=input("enter the name of the new employee: ")

print(employees)




