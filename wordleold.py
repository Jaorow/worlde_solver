import os

def read_file(filename):
    f = open(filename)
    contents = f.read().splitlines()
    f.close()
    return contents

def startup():
    os.system('clear')
    input("please answer the questions below with Y for yes or N for no (press Q to quit)\nPress and button to continue... ")
    contents = read_file("words.txt")
    return contents

def known_position_letter(contents):
    while True:
        location = input("What is the position you know: ")
        try:
            location = int(location)-1
            if 0 <= location <= 4:
                break
            else: 
                print("you did not enter a number in the right range try again.")
                continue

        except ValueError:
            print("you did not enter a number try again.")




    letter = input("What is the letter: ").lower()
    new_contents = []
    for i in contents:
        if i[location] == letter:
            new_contents.append(i)
        else: continue

    return new_contents

def known_letter(contents):
    inp = input("What is the letter you know is in the word: ").lower()

    while True:
        location = input("What is the position you know: ")
        try:
            location = int(location)-1
            if 0 <= location <= 4:
                break
            else: 
                print("you did not enter a number in the right range try again.")
                continue

        except ValueError:
            print("you did not enter a number try again.")
    
    new_contents = []
    for i in contents:
        if inp in i:
            if i[location] != inp:
                new_contents.append(i)
        else: continue
    print("")
    return new_contents

def known_not_letter(contents):
    inp = input("What is a letter you know is not in the word: ").lower()
    new_contents = []
    for i in contents:
        if inp in i:
            pass
        elif inp not in i:
            new_contents.append(i)

    return new_contents

def show_words(words):
        print("\nThe words are :\n")
        count = 0 
        for i in words:
            count += 1
            if count < 8:
                footer = ", "
            else:
                footer = "\n"
                count = 0
            print(i,end = footer)
        if len(words) > 20:
            print("\n\nWOW thats a lot of words, Who knows how that will help!\n")
        wait = input("\nPress any button to continue... ")

def menu(words):
    
    while True:
        os.system('clear')
        print("(Yes = Y, No = N)")
        print(f"\nThere is {len(words)} word{'s' if len(words)>1 else ''}.\n")
        inp = input("(Press Q to quit or S to show words)\nIf you know the position of a letter please press 1. \nIf you know a letter that is not in the wordle please press 2.\nIf you know a letter that is in the wordle but not its position please press 3.\n\n----ANSWER----> ").lower()
        if inp == "1":
            return known_position_letter(words)
        if inp == "2":
            return known_not_letter(words)
        if inp == "3":
            return known_letter(words)
        if inp == "S" or inp == "s":
            show_words(words)
            continue
        if inp == "q":
            return False

        if inp != "1" or inp != "2" or inp != "3": 
            print("Sorry input was not valid.")

def main():
    words = startup()
    while words != False:
        words = menu(words)

    print("\n=================\nTHANKS FOR COMING\n=================\n")

main()