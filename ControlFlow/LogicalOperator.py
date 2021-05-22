
high_income = True
good_credit = False
student = True

if (high_income or good_credit) and not student:
    message = "Eligible"
else:
    message = "Not eligible"

print(message)
