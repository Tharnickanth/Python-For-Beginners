

def fizz_buzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


number = int(input("Enter the number : "))
print(fizz_buzz(number))
