def task_1():
    """Ask for the user’s first name
    and display the output message Hello [First Name] . """
    name = input("Enter your name:")
    return f"Hi, {name}"


def task_2():
    """Ask for the user’s first name
    and then ask for their surname and display the output message"""
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    return "Hello, {} {}".format(name, surname)


def task_3():
    """Write code that will display the joke “What do you call a bear with no teeth?”
    and on the next line display the answer “A gummy bear!”
    Try to create it using only one line of code."""
    joke = "What do you call a bear with no teeth?\n" \
           "A gummy bear!"
    return joke


def task_4():
    """Ask the user to enter two numbers.
    Add them together and display the answer as The total is [answer]."""
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    return str("The total is " + str(c))


def task_5():
    """Ask the user to enter three numbers.
    Add together the first two numbers and then multiply this total by the third.
    Display the answer as The answer is [answer]"""
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    d = (a + b) * c
    return str("The answer is {}".format(d))


def task_6():
    """Ask how many slices of pizza the user started with
    and ask how many slices they have eaten.
    Work out how many slices they have left
    and display the answer in a userfriendly format"""
    a = int(input("How many slices of pizza you started with? "))
    b = int(input("How many slices have you eaten? "))
    c = a - b
    return f"There are(is) {c} slice(s) left"


def task_7():
    """Ask the user for their name and their age.
    Add 1 to their age and display the output [Name] next birthday you will be [new age]"""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    new_age = age + 1
    return f"{name}, next birthday you will be {new_age}"


def task_8():
    """Ask for the total price of the bill,
    then ask how many diners there are.
    Divide the total bill by the number of diners
    and show how much each person must pay. """
    price = int(input("Enter bill price: "))
    dinners = int(input("Enter count of dinners: "))
    pay_per_person = price / dinners
    return f"Each person must pay {pay_per_person}"


def task_9():
    """Write a program that will ask for a number of days
    and then will show how many hours,
    minutes and seconds are in that number of days."""
    days = int(input("Enter number of days: "))
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return f"In {days} there are {hours} hours, {minutes} minutes or {seconds} seconds."


def task_10():
    """There are 2,204 pounds in a kilogram.
    Ask the user to enter a weight in kilograms and convert it to pounds."""
    kg = int(input("Enter a weight in kg: "))
    pounds = kg * 2.204
    return f"{kg} is {pounds}"


def task_11():
    """Task the user to enter a number over 100
    and then enter a number under 10 and tell them how many times
    the smaller number goes into the larger number in a user-friendly format."""
    over_number = int(input("Enter a number over 100: "))
    under_number = int(input("Enter a number under 10: "))
    result = over_number // under_number
    return f"{under_number} goes into {over_number} for {result} times!"
