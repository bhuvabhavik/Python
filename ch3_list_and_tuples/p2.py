#write a program to accept marks of 6 students and display then in a sorted manner


print("Enter marks of 3 student")

marks1 = int(input("Enter marks of Student 1 : "))
marks2 = int(input("Enter marks of Student 2 : "))
marks3 = int(input("Enter marks of Student 3 : "))
marks4 = int(input("Enter marks of Student 4 : "))
marks5 = int(input("Enter marks of Student 5 : "))
marks6 = int(input("Enter marks of Student 6 : "))


studentMarksList = [marks1,marks2,marks3,marks4,marks5,marks6]

studentMarksList.sort()

print(studentMarksList)
