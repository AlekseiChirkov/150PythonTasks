def task_12():
    """Ask for two numbers. If the first one is larger than the second,
    display the second number first and then the
    first number, otherwise show the first number first and then the second"""
    num1 = int(input("Enter first num: "))
    num2 = int(input("Enter second num: "))
    if num1 > num2:
        return num2, num1
    else:
        return num1, num2


def task_13():
    """Ask the user to enter a number that is under 20.
    If they enter a number that is 20 or more,
    display the message “Too high”, otherwise display “Thank you”"""
    num = int(input("Enter a number that is under 20: "))
    if num < 20:
        return "Thank you!"
    else:
        return "Too high!"


def task_14():
    """Ask the user to enter a number between 10 and 20 (inclusive).
    If they enter a number within this range,
    display the message “Thank you”, otherwise display the message “Incorrect answer”."""
    num = int(input("Enter a number between 10 and 20: "))
    if 10 <= num <= 20:
        return "Thank you!"
    else:
        return "Incorrect answer!"


def task_15():
    """Ask the user to enter their favourite colour.
    If they enter “red”, “RED” or “Red” display the message
    “I like red too”, otherwise display the message
    “I don’t like [colour], I prefer red”. """
    color = input("Enter your favorite color: ")
    if color.lower() == "red":
        return "I like it too!"
    else:
        return f"I don't like {color}, I prefer red."


def task_16():
    """Ask the user if it is raining and
    convert their answer to lower case so it doesn’t matter
    what case they type it in. If they answer “yes”,
    ask if it is windy. If they answer “yes” to this second question,
    display the answer “It is too windy for an umbrella”,
    otherwise display the message “Take an umbrella”.
    If they did not answer yes to the first question,
    display the answer “Enjoy your day”."""
    rain = input("Is it rain? ")
    if rain.lower() == "yes":
        wind = input("Is it windy? ")
        if wind.lower() == "yes":
            return "It's too windy for an umbrella."
        else:
            return "Take an umbrella."
    else:
        return "Enjoy your day!"


def task_17():
    """Ask the user’s age.
    If they are 18 or over, display the message “You can vote”,
    if they are aged 17, display the message “You can learn to drive”,
    if they are 16, display the message “You can buy a lottery ticket”,
    if they are under 16, display the message “You can go Trickor-Treating”."""
    age = int(input("How old are you? "))
    if age >= 18:
        return "You can vote."
    elif age == 17:
        return "You can learn to drive."
    elif age == 16:
        return "You can buy a lottery ticket"
    else:
        return "You can go Trickor-Treating"


def task_18():
    """Ask the user to enter a number.
    If it is under 10, display the message “Too low”,
    if their number is between 10 and 20, display “Correct”,
    otherwise display “Too high”."""
    num = int(input("Enter a number, please: "))
    if num < 10:
        return "To low!"
    elif 10 <= num <= 20:
        return "Correct!"
    else:
        return "To high!"


def task_19():
    """Ask the user to enter 1, 2 or 3.
    If they enter a 1, display the message “Thank you”,
    if they enter a 2, display “Well done”,
    if they enter a 3, display “Correct”.
    If they enter anything else, display “Error message”."""
    num = int(input("Enter 1, 2 or 3: "))
    if num == 1:
        return "Thank you!"
    elif num == 2:
        return "Well done!"
    elif num == 3:
        return "Correct!"
    else:
        return "Error message!"
