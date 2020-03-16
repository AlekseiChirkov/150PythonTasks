def task_35():
    """Ask the user to enter their name and then display their name three times."""
    name = input("Enter your name: ")
    for i in range(3):
        print(name)

    return "End"

def task_36():
    """Alter program 035 so that it will ask the user to enter their name
    and a number and then display their name that number of times. """
    name = input("Enter your name: ")
    num = int(input("Enter a number: "))
    for i in range(num):
        print(name)

    return "End"

def task_37():
    """Ask the user to enter their name and
    display each letter in their name on a separate line."""
    name = input("Enter your name: ")
    for i in name:
        print(i)

    return "End"

def task_38():
    """Change program 037 to also ask for a number.
    Display their name (one letter at a time on each line)
    and repeat this for the number of times they entered"""
    name = input("Enter your name: ")
    num = int(input("Enter a number: "))
    for p in range(num):
        for i in name:
            print(i)
        print('-----')

    return "End"

def task_39():
    """Ask the user to enter a number between 1 and 12
    and then display the times table for that number. """
    num = int(input("Enter a number between 1 and 12: "))
    for i in range(1, 11):
        print(str(num) + "*" + str(i) + "=" + str(num * i))

    return "End"

def task_40():
    """Ask for a number below 50 and then count down from 50 to that number,
    making sure you show the number they entered in the output."""
    number = int(input("Enter a number below 50: "))
    for i in range(50, number-1, -1):
        print(i)

    return "End"

def task_41():
    """Ask the user to enter their name and a number.
    If the number is less than 10, then display their name that number of times;
    otherwise display the message “Too high” three times."""
    name = input("Enter your name: " )
    number = int(input("Enter a number: "))
    if number < 10:
        for i in range(number):
            print(name)
    else:
        for j in range(3):
            print("Too high")

    return "End"

def task_42():
    """Set a variable called total to 0.
    Ask the user to enter five numbers and after each input ask them
    if they want that number included.
    If they do, then add the number to the total.
    If they do not want it included, don’t add it to the total.
    After they have entered all five numbers, display the total. """
    total = 0
    print("Enter five numbers: ")
    for i in range(5):
        number = int(input())
        print("Do you want to include it to total?")
        answer = input("Answer 'yes' or 'no': ")
        if answer.lower() == 'yes':
            total += number

    print("The total is: " + str(total))
    return "End"

def task_43():
    """Ask which direction the user wants to count (up or down).
    If they select up, then ask them for the top number
    and then count from 1 to that number.
    If they select down, ask them to enter a number below 20
    and then count down from 20 to that number.
    If they entered something other than up or down,
    display the message “I don’t understand”. """
    direction = input("Which direction do you want to count?\n"
                      "Write 'up' or 'down': ")
    if direction.lower() == 'up':
        number = int(input("Enter a top number: "))
        for i in range(number+1):
            print(i)
    elif direction.lower() == 'down':
        number = int(input("Enter a number that is below 20: "))
        for i in range(20, number-1, -1):
            print(i)
    else:
        print("I don't understand.")

    return "End"

def task_44():
    """Ask how many people the user wants to invite to a party.
    If they enter a number below 10,
    ask for the names and after each name display “[name] has been invited”.
    If they enter a number which is 10 or higher,
    display the message “Too many people”."""
    people = int(input("How many people you want to invite: "))
    if people < 10:
        for i in range(people):
            name = input("Enter a name: ")
            print(f"{name} has been invited.")
    else:
        print("Too many people.")

    return "End"
