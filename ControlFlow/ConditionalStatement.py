
Marks = int(input("Enter your Marks : "))

if Marks > 75:
    Grade = "A"
elif Marks > 65:
    Grade = "B"
elif Marks > 55:
    Grade = "C"
elif Marks > 35:
    Grade = "S"
else:
    Grade = "F"
print(f"Your Grade : {Grade}")
