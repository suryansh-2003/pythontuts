total = 0

t = int(input ("Enter total marks (Out of which, marks are obtained) : "))

print ("Enter marks of each subject :---------------")

for i in range (3):
    a = int(input("Enter marks of subject : "))

if a > t:
    print ("Obtained marks exceeded total marks!")

else:
    total += a

p = (total*100)/(3*t)

print ("Percentage obtained = ", p)