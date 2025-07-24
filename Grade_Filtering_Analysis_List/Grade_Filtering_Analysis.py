#Case Study Title:Study Grade Filtering Using List Comprehension
'''Problem Statement:
A college wants to automate the process of filtering students based on their grades and analyze performance metrics efficiently using Python.
The system should be able to:
1.Filter students who scored above a certain grade.
2.Assign pass/fail status.
3.Calculate squared grades for performance indexing.
4.Identify top performers.
Create a list of students who need remedial classes.'''


students = [("Aarav",82),("Bhavna",56),("Sita",91),("Raju",36),("Harshita",48),("Aditi",63),("Tina",43)]
pass_mark=40
remedial_threshold=50
top_performance=85

# Filter students who scored above a certain grade.
above_60=[name for name,grade in students if grade > 60]
print("Students scoring above 60:",above_60)


# Assign pass/fail status.
pass_fail_status=[(name,"Pass" if grade>=pass_mark else "Fail")for name,grade in students ]
print("Pass/Fail status",pass_fail_status)


#Calculate squared grades for performance indexing.
square_grades = [(name, grade**2) for name, grade in students]
print("Sqaure of grades",square_grades)


#Identify top performers.
top_performers=[name for name,grade in students if grade >=85]
print("Students scoring above 85:",top_performers)

#List of students who need remedial classes
remedial_students=[name for name,grade in students if grade<50]
print("Students who need remedial:",remedial_students)
