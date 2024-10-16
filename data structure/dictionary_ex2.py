students=dict()
n=int(input("Enter number of students :"))
for i in range(n):
    stuname =input("enter names of students :")
    marks=[]
    for j in range (5):
        mark=float(input("enter the marks of subjects :"))
        marks.append(mark)
    students[stuname]=marks
print("dictionary of students created :")
print(students)
