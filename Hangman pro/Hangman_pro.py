
# Create a simple dictionary of words
import random
my_dictionary = {
    'k1':"serendipity",
    'k2':"phenomenon",
    'k3':"quarantine",
    'k4':"maverick",
    'k5':"nostalgia",
    'k6':"labyrinth",
    'k7':"cryptic",
    'k8':"chimera",
    'k9':"euphoric",
    'k10':"paradox"
    }


# This function selects a random word from the dictionary
def random_word():

    randomword = random.choice(list(my_dictionary.values()))

    return randomword

# This is a display for the length of the word to guide the user
def word_len(randomword):

    output = "_ "*len(randomword)

    return output[:-1] #cuts out the last space
    

# User input
def guess_():

    choice = input("Choose a letter: a-z\n")

    return choice 


def find_indexes():

    global no_of_attempts 

    start = 0 
    seen_indexes = []

    while start <= len(myrandomword):
        
        random_ = myrandomword.find(guess,start) 

        if random_ == -1:
            break
        else:
            seen_indexes.append(random_)
            start = random_ + 1 #This makes reference to where random_ currently is in the string

    if not seen_indexes: #If list is empty 
        print("oops! wrong guess!")
        no_of_attempts += 1 

    return seen_indexes

# Visual display function

def display_word():
    wordlist = [char for char in wordlength]

    for index_value in seen_indexes:

        wordlist[index_value*2] = guess #This adjustment is necessary for the visual representation of the string

    return ''.join(wordlist)

def game_reset():
    pass



def replay():

    choice = "RANDOM"

    while choice not in ['y','n']:

        choice = input("Play again Y or N?").lower()

        if choice not in ['y','n']:
            print("Invalid input.. Y or N ?")

        if choice == "y":
            #Reset the game
            return True
        else:
            print("Thanks for playing!")
            return False


# GAME LOGIC
game_on = True

while game_on:


    print("Welcome to Hangman Survival!")

    no_of_attempts = 0

    myrandomword = random_word()

    wordlength = word_len(myrandomword)
    print(wordlength)
    print("")
    print("fill up the blank spaces to win!")
    print("")
    print("You have 6 attempts only.")


    while True:

        guess = guess_()
        seen_indexes = find_indexes()

        wordlength = display_word().upper()
        print(wordlength)

        if "_" not in wordlength:
            print("You win!")
            break
        if no_of_attempts == 1:
            print(" O ")
        elif no_of_attempts ==2:
            print(" O ")
            print('\ ')
        elif no_of_attempts ==3:
            print(" O ")
            print('\ /')
        elif no_of_attempts == 4:
            print(" O ")
            print('\ /')
            print(' | ')
        elif no_of_attempts == 5:
            print(" O ")
            print('\ /')
            print(' | ')
            print("/  ")

        elif no_of_attempts == 6:
            print("Maximum no. of attempts reached!")
            print("")
            print(" O ")
            print('\ /')
            print(' | ')
            print("/ \ ")
            print("You lose!")
            print(f"{myrandomword.upper()}") #This prints out the word at the end
            break

    game_on = replay()


