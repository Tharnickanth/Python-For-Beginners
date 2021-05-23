number = 100
while number > 0:
    print(number)
    number //= 2


comment = ""

while comment.lower() != "quit":
    comment = input(">>")


# Infinite Loop

while True:
    comment = input(">>")
    if comment.lower() == "quit":
        break
