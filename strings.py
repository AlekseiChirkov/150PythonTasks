def task_20():
    """Ask the user to enter their first name
    and then display the length of their name."""
    name = input("Enter your name: ")
    return len(name)


def task_21():
    """Ask the user to enter their first name
    and then ask them to enter their surname.
    Join them together with a space between
    and display the name and the length of whole name."""
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    full_name = name + " " + surname
    return full_name, len(full_name)


def task_22():
    """Ask the user to enter their first name and surname in lower case.
    Change the case to title case and join them together.
    Display the finished result"""
    name = input("Enter your name in lower case: ")
    surname = input("Enter your surname in lower case: ")
    full_name = name.title() + " " + surname.title()
    return full_name


def task_23():
    """Ask the user to type in the first line of a nursery rhyme
    and display the length of the string.
    Ask for a starting number and an ending number
    and then display just that section of the text
    (remember Python starts counting from 0 and not 1)."""
    rhyme = input("Enter a nursery rhyme: ")
    print("This rhyme has " + str(len(rhyme)) + " characters.")
    start = int(input("Enter a start num: "))
    end = int(input("Enter an end num: "))
    return rhyme[start:end]


def task_24():
    """Ask the user to type in any word and display it in upper case. """
    word = input("Enter any word: ")
    return word.upper()


def task_25():
    """Ask the user to enter their first name.
    If the length of their first name is under five characters,
    ask them to enter their surname and join them together
    (without a space) and display the name in upper case.
    If the length of the first name is five or more characters,
    display their first name in lower case."""
    name = input("Enter your first name: ")
    if len(name) < 5:
        surname = input("Enter your surname: ")
        full_name = name + surname
        return full_name.upper()
    else:
        return name.lower()


def task_26():
    """Pig Latin takes the first consonant of a word,
    moves it to the end of the word and adds on an “ay”.
    If a word begins with a vowel you just add “way” to the end.
    For example, pig becomes igpay, banana becomes ananabay,
    and aadvark becomes aadvarkway.
    Create a program that will ask the user to enter a word and change it into Pig Latin.
    Make sure the new word is displayed in lower case."""
    word = input("Enter a word: ")
    start = word[0]
    rest = word[1:len(word)]
    if start != "a" and start != "o" and start != "u" and start != "e" and start != 'i':
        return rest + start + "ay"
    else:
        return word + "way"

print(task_26())