import random

def task_52():
    """Display a random integer between 1 and 100 inclusive. """
    integer = random.randint(1, 101)
    return integer

def task_53():
    """Display a random fruit from a list of five fruits"""
    fruit = random.choice(['apple', 'pear', 'pineapple', 'orange', 'kiwi'])
    return fruit

def task_54():
    """Randomly choose either heads or tails (“h” or “t”).
    Ask the user to make their choice.
    If their choice is the same as the randomly selected value,
    display the message “You win”, otherwise display “Bad luck”.
    At the end, tell the user if the computer selected heads or tails. """
    choose = random.choice(['h', 't'])
    player = input("Choose 'h' or 't': ")
    if choose == player:
         print("You win!")
    else:
        print("Bad luck!")

    return f"Computer selected {choose}"

def task_55():
    """Randomly choose a number between 1 and 5.
    Ask the user to pick a number.
    If they guess correctly, display the message “Well done”,
    otherwise tell them if they are too high or too low
    and ask them to pick a second number.
    If they guess correctly on their second guess,
    display “Correct”, otherwise display “You lose”. """
    random_number = random.randint(1, 6)
    user_choice = int(input("Enter a number between 1 and 5: "))
    if random_number == user_choice:
        print("Well done!")
    elif random_number > user_choice:
        print("Too low!")
        while True:
            user_choice = int(input("Enter a number between 1 and 5: "))
            if random_number == user_choice:
                print("Correct!")
                break
            elif random_number > user_choice:
                print("Too low, try again!")
            else:
                print("Too high, try again!")
    else:
        print("Too high!")
        while True:
            user_choice = int(input("Enter a number between 1 and 5: "))
            if random_number == user_choice:
                print("Correct!")
                break
            elif random_number > user_choice:
                print("Too low, try again!")
            else:
                print("Too high, try again!")

    return "End"

def task_56():
    """Randomly pick a whole number between 1 and 10.
    Ask the user to enter a number and keep entering numbers
    until they enter the number that was randomly picked."""
    number = random.randint(1, 11)
    while True:
        user_choice = int(input("Enter a number: "))
        if number == user_choice:
            print("You're right!")
            break

    return "End"

def task_57():
    """Update program 056 so that it tells the user
    if they are too high or too low before they pick again"""
    number = random.randint(1, 11)
    while True:
        user_choice = int(input("Enter a number: "))
        if number == user_choice:
            print("You're right!")
            break
        elif number > user_choice:
            print("Too low!")
        else:
            print("Too high!")

    return "End"

def task_58():
    """Make a maths quiz that asks five questions by randomly generating
    two whole numbers to make the question (e.g. [num1] + [num2]).
    Ask the user to enter the answer. If they get it right add a point to their score.
    At the end of the quiz, tell them how many they got correct out of five."""
    points = 0
    count = 0
    while True:
        number1 = random.randint(1, 11)
        number2 = random.randint(1, 11)
        print(f"Answer the question: {number1} + {number2}")
        total = number1 + number2
        answer = int(input("Enter your answer: "))
        if answer == total:
            points += 1
        elif answer != total:
            print(f"Answer is: {total}")
            print("Try again!")
        count += 1
        if count == 5:
            print(f"Your points is: {points}")
            break

    return "End"

def task_59():
    """Display five colours and ask the user to pick one.
    If they pick the same as the program has chosen,
    say “Well done”, otherwise display a witty answer which involves the correct colour,
    e.g. “I bet you are GREEN with envy” or “You are probably feeling BLUE right now”.
    Ask them to guess again; if they have still not got it right,
    keep giving them the same clue
    and ask the user to enter a colour until they guess it correctly."""
    colors = ['Green', 'Blue', 'Red', 'White', 'Black']
    print(colors)
    while True:
        random_color = str(random.choice([colors[0], colors[1], colors[2], colors[3], colors[4]]))
        user_choice = input(f"Enter a one color {colors}: ")
        if random_color.lower() == user_choice.lower():
            print("Well, done!")
            break
        else:
            print(random.choice(
                [
                    f"I bet you are {random_color} with envy",
                    f"You are probably feeling {random_color} right now",
                    f"Today is {random_color} weather"
                ]
            ))

    return "End"


print(task_59())