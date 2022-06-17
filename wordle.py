import os
from word import words

def startup():
    print(f"Hi {os.getlogin()} Welcome to wordle solver 5000")
    input("Press return to start ")
    os.system('clear')

def menu(obj):
    while True:
        os.system('clear')
        print(f"Welcome to the menu \n\nThere is currently {obj.length()}.\n")
        print("(Press S to show, R to restore, Q to quit, or M for deep-menu)\n")
        print("Press 1 for letters not in the word\nPress 2 for letters you know the position of\nPress 3 for letters you know are in the word but are not in the right position\n")
        inp = input("-----> ").upper()
        if inp in "sSrRqQ123Mm":
            return inp
        else:
            print("That was not a valid input")
            input("Press enter to try agian ")

def main():
    os.system('clear')
    startup()
    obj = words()
    inp = None
    while inp !="Q":
        inp = menu(obj)
        if inp == "S":
            print(obj)
            input("Press enter to continue... ")
        elif inp == "R":
            message = obj.restore()
            input(f"{message}\nPress enter to continue")

        elif inp == "1":
            num = input("What letters do you know are not in the word --> ")
            obj.nul(num)

        elif inp == "2":
            letter = input("what is the letter you know --> ")
            num = input("What is the possition you know --> ")
            obj.pos(num,letter)

        elif inp == "3":
            letter = input("What is the letter you know --> ")
            num = input(f"What is the possition you know {letter} is not --> ")
            obj.let(num,letter)
        
        elif inp == "M":
            obj.menu()


    print(f"\n\n{'='*19}\n THANKS FOR COMING \n{'='*19}\n\n")

main()