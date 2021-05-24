# Keyword Argument

def getMessage(name, age):
    return f"I\'m {name}, I\'m {age} years old"


message = getMessage(age=25, name="Tharnickanth")
print(message)


def increment(number, by=25):
    return number+by


total = increment(100, 1000)
print(total)


def multiply(*number):
    total = 1
    for num in number:
        total *= num

    return total


print(multiply(2, 4, 5, 7))


def details(**user):
    print(user)


details(name="Tharnickanth", age=34, address="Kalmunai")
