def task_45():
    """Set the total to 0 to start with.
    While the total is 50 or less,
    ask the user to input a number.
    Add that number to the total and print the message “The total is… [total]”.
    Stop the loop when the total is over 50 . """
    total = 0
    while total < 50:
        number = int(input("Enter a number: "))
        total += number
        print(f"The total is {total}")

    return "End"

def task_46():
    """Ask the user to enter a number.
    Keep asking until they enter a value over 5
    and then display the message “The last number you entered was a [number]”
    and stop the program"""
    number = 0
    while number <= 5:
        number = int(input("Enter a number: "))
        if number > 5:
            print(f"The last number you entered was a {number}")
            break

    return "End"

def task_47():
    """Ask the user to enter a number and then enter another number.
    Add these two numbers together and then ask if they want to add another number.
    If they enter “y", ask them to enter another number
    and keep adding numbers until they do not answer “y”.
    Once the loop has stopped, display the total."""
    first = int(input("Enter a 1st number: "))
    second = int(input("Enter a 2nd number: "))
    total = first + second
    answer = input("Do tou want to add another number? (y/n): ")
    while answer.lower() == 'y':
        total += int(input("Add another number: "))
        answer = input("Do tou want to add another number? (y/n): ")
        if answer.lower() != 'y':
            print(f"The total is {total}")
            break

    return "End"

def task_48():
    """Ask for the name of somebody the user wants to invite to a party.
    After this, display the message “[name] has now been invited”
    and add 1 to the count. Then ask if they want to invite somebody else.
    Keep repeating this until they no longer want to invite anyone else to the party
    and then display how many people they have coming to the party."""
    count = 0
    list_of_persons = []
    answer = input("Do you want invite someone? (y/n) ")
    while  answer.lower() == 'y':
        person = input("Who do you want to invite? Enter a name: ")
        count += 1
        list_of_persons.append(person)
        answer = input("Do you want invite someone more? (y/n) ")
        if answer.lower() != 'y':
            print(f"You have invited {count} people.")
            print(f"You have invited next persons: {list_of_persons}")
            break

    return "End"


def task_49():
    """Create a variable called compnum and set the value to 50.
    Ask the user to enter a number.
    While their guess is not the same as the compnum value,
    tell them if their guess is too low or too high and ask them to have another guess.
    If they enter the same value as compnum,
    display the message “Well done, you took [count] attempts”. """
    compnum = 50
    number = int(input("Enter a number: "))
    count = 0
    while True:
        count += 1
        if number < compnum:
            print("Too low.")
            number = int(input("Enter another number: "))
        elif number > compnum:
            print("Too high.")
            number = int(input("Enter another number: "))
        else:
            print(f"Well done, you took {count} attempts")
            break

    return "End"

def task_50():
    """Ask the user to enter a number between 10 and 20.
    If they enter a value under 10, display the message “Too low”
    and ask them to try again. If they enter a value above 20,
    display the message “Too high” and ask them to try again.
    Keep repeating this until they enter a value that is between 10 and 20
    and then display the message “Thank you”."""
    number = int(input("Enter a number between 10 and 20: "))
    while True:
        if number < 10:
            print("Too low.")
            number = int(input("Enter another number: "))
        elif number > 20:
            print("Too high.")
            number = int(input("Enter another number: "))
        else:
            print("Thank you")
            break

    return "End"

def task_51():
    """Using the song “10 green bottles”,
    display the lines “There are [num] green bottles hanging on the wall,
    [num] green bottles hanging on the wall,
    and if 1 green bottle should accidentally fall”.
    Then ask the question “how many green bottles will be hanging on the wall?”
    If the user answers correctly, display the message
    “There will be [num] green bottles hanging on the wall”.
    If they answer incorrectly,
    display the message “No, try again” until they get it right.
    When the number of green bottles gets down to 0,
    display the message “There are no more green bottles hanging on the wall”."""

    num = 10
    while True:
        print(f"There are {num} green bottles hanging on the wall,\n"
        f"{num} green bottles hanging on the wall,\n"
        "and if 1 green bottle should accidentally fall")

        answer = int(input("How many green bottles will be hanging on the wall? "))



print(task_51())