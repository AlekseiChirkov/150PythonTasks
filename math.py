import math

def task_27():
    """Ask the user to enter a number with lots of decimal places.
    Multiply this number by two and display the answer"""
    num = float(input("Enter a number with a lot of decimal places: "))
    res = num * 2
    return res


def task_28():
    """Update program 027 so that it will display the answer to two decimal places. """
    num = float(input("Enter a number with a lot of decimal places: "))
    res = num * 2
    return round(res, 2)


def task_29():
    """Ask the user to enter an integer that is over 500.
    Work out the square root of that number and display it to two decimal places."""
    num = int(input("Enter a number that is over 500: "))
    root = math.sqrt(num)
    return root


def task_30():
    """Display pi (π) to five decimal places."""
    pi = math.pi
    return round(pi, 5)


def task_31():
    """Ask the user to enter the radius of a circle
    (measurement from the centre point to the edge).
    Work out the area of the circle (π*radius2)."""
    rad = int(input("Enter a radius of circle: "))
    area = math.pi * rad**2
    return area


def task_32():
    """Ask for the radius and the depth of a cylinder and work out the total volume
    (circle area*depth) rounded to three decimal places."""
    rad = int(input("Enter a radius of a cylinder: "))
    depth = int(input("Enter a depth of a cylinder: "))
    total = (math.pi * rad**2) * depth
    return round(total, 3)


def task_33():
    """Ask the user to enter two numbers.
    Use whole number division to divide the first number by the second
    and also work out the remainder and display the answer in a user-friendly way
    (e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”). """
    num1 = int(input("Enter a number 1: "))
    num2 = int(input("Enter a number 2: "))
    whole = num1 // num2
    remain = num1 % num2
    return f"{num1} devided by {num2} is {whole} with {remain} remaining!"


def task_34():
    """Display the following message:

    1) Square
    2) Triangle
    Enter a number:

    If the user enters 1,
    then it should ask them for the length of one of its sides and display the area.
    If they select 2, it should ask for the base and height of the triangle
    and display the area.
    If they type in anything else, it should give them a suitable error message. """
    print("1) Square\n2) Triangle\n")
    num = int(input("Enter a number: "))
    if num == 1:
        length = int(input("Enter a length of one side: "))
        square = length*length
        return square
    elif num == 2:
        height = int(input("Enter a height of triangle: "))
        base = int(input("Enter a base of triangle: "))
        triangle = (base * height) / 2
        return triangle
    else:
        return "Type error!"

print(task_34())