run = True
birthdays = []


def wrong_input():
    print("\nWrong input.")
    print("Try again.\n")


def question():
    print(f"Current birthdays in database: {birthdays}")
    print("Type in your birthday like this: dd/mm/yyyy\n")
    birthday = input()
    birthdayCheck = birthday.split("/")
    try:
        if len(birthdayCheck) == 3 \
                and len(birthdayCheck[0]) == 2 \
                and len(birthdayCheck[1]) == 2 \
                and len(birthdayCheck[2]) == 4\
                and birthdayCheck[0].isdigit()\
                and birthdayCheck[1].isdigit()\
                and birthdayCheck[2].isdigit():
            if birthday in birthdays:
                print("\n!We have a pair!\n")
            else:
                birthdays.append(birthday)
        else:
            wrong_input()
    except IndexError:
        wrong_input()


def decision():
    print("\nYou want to continue?\ny/n?")
    a = input()
    if a == "y":
        print("Okay, lets go!")
    else:
        print("Alright. By!")
        exit()


if __name__ == "__main__":
    print("Hello,")
    while run:
        question()
        decision()
