# for
for number in range(3):
    print("attempt", number+1, "."*(number+1))


# for-Else
successfull = False
for number in range(5):
    print("Attempt", number+1)
    if(number == 2):
        successfull = True
    if successfull:
        break
else:
    print("5 time Attempted")

# for-Nested

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
