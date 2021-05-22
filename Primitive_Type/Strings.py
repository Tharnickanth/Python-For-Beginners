# strings...

Name = "Tharnickanth Manoranjan"

print(Name)
print(Name[0:12])
print(Name[13:])
print(Name[3:16])


Letter = """
Hi Tharnickanth,

How are you.....

.......................
...................
.......................

"""

print(Letter)

Course = "Learning \nPython \nfor \nBeginners"
print(Course)
print(len(Course))

# formatted strings
fName = "Tharnickanth"
lName = "Manoranjan"
fullName = fName+" "+lName
print(fullName)
print(f"{fName} {lName}")
print(f"{len(fName)} {lName}")

# String Methods

course = " python programming "
print(course.upper())
print(course.lower())
print(course. title())
print(course.strip())
print(course.rstrip())
print(course.lstrip())
print("pro" in course)
print("the" not in course)
