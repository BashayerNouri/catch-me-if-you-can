from termcolor import colored
import os
import random
import time


picture = ['''
                +---+
                |   |
               _O_  |
                |   |
               / \  |
                    |
              =========''', 
        '''
                +---+
                    |
                    |
               \O/  |
                |   |
               | |  |
              =========''']



class Score:
    def __init__(self, level_selection, name):
        self.level_selection = level_selection
        self.name = name
        self.bonus = 5
        self.word = len(random_word) 

    def get_score(self):
        if self.level_selection == 1:
            return (self.level_selection * 10 + self.bonus + self.word)
        elif self.level_selection == 2:
            return (self.level_selection * 20 + self.bonus + self.word)
        else:
            return (self.level_selection * 30 + self.bonus + self.word)

    def __str__(self):
        return "\n+---------------+\nName: %s \nLevel: %s \nScore: %s \n+---------------+" % (self.name, self.level_selection, self.get_score())


def get_random_word():
    file = open("wordlist.txt", "r")
    words = file.readlines() 
    random_word = random.choice(words)
    random_word = random_word.strip("\n")
    random_word = random_word.strip("\r")
    random_word = random_word.lower()
    file.close()
    return random_word


random_word = get_random_word()


def weclcome_message():
    messsages = ["\nWelcome to Catch Me If You Can","Get ready","Starting the game...","Selecting a word..."]
    os.system("cls")
    for messsage in messsages:
        print (colored(messsage, 'yellow'))
        time.sleep(1.3)


def play_again():
    print(colored("\nWould you like to play again?", 'cyan'))
    time.sleep(1)

    while True:
        answer = input(colored("If yes enter \"yes\" or \"y\". If no enter \"no\" or \"n\" ", 'cyan')).lower()

        if answer == "y" or answer == "yes":
            main()
        elif answer == "n" or answer == "no":
            break
        else:
            print("Please enter \"yes\" or \"y\" or \"no\" or \"n\" ")
            time.sleep(1)


def main():

    os.system("cls")

    level = { 
    'beginner': {'tries': 10},
    'immediate': {'tries': 8},
    'expert': {'tries': 6}
    }

    letters_guessed = []
    guessed = False
    selection = False

    print("\nThere are multiple difficulty settings shown below:")
    time.sleep(1)
    print(colored("\t1. Beginner (10 lives)", 'green'))
    time.sleep(1)
    print(colored("\t2. Intermediate (8 lives)", 'yellow'))
    time.sleep(1)
    print(colored("\t3. Expert (6 lives)", 'red'))
    time.sleep(1)

    
    while selection == False:
        level_selection = input(colored("\nSelect A Level: ", 'cyan'))  
        try:
            level_selection = int(level_selection)
            if level_selection == 1:
                tries = level['beginner']['tries']
                selection = True
            elif level_selection == 2:
                tries = level['immediate']['tries']
                selection = True
            elif level_selection == 3:
                 tries = level['expert']['tries']
                 selection = True
            else:
                print(colored("Please select a number from 1 to 3...", 'yellow'))
        except ValueError:
                print(colored("You didn't enter a number!", 'yellow'))


    name = input(colored("\nEnter a name, nickname or team name: ", 'cyan'))


    weclcome_message()


    print("\nThe word contains", len(random_word), 'letters. \n')
    print(len(random_word) * colored(" _", 'green'))

    
    while guessed == False and tries > 0:
            print(colored("\nYou have %s tries." % str(tries), 'magenta'))
            guess = input("\nEnter one letter or the full word: ").lower()

            # Case 1: if the player enters a single letter.
            if len(guess) == 1:
                if not guess.isalpha():
                    print(colored("\n\'%s\' is not a letter, enter a letter!\n" % guess, 'yellow'))
                    print(colored("\nLetters Guessed: %s\n" % letters_guessed, 'red'))

                elif guess in letters_guessed:
                    print(colored("\n\'%s\' has been guessed before, try another letter.\n" % guess, 'yellow'))
                    print(colored("\nLetters Guessed: %s\n" % letters_guessed, 'red'))

                elif guess not in random_word:
                    print(colored("\n\'%s\' is not part of the word, try another letter.\n" % guess, 'yellow'))
                    letters_guessed.append(guess)
                    tries -=1
                    print(colored("\nLetters Guessed: %s\n" % letters_guessed, 'red'))

                elif guess in random_word:
                    print(colored("\nWell done, that letter exists in the word!\n", 'yellow'))
                    letters_guessed.append(guess)
                    print(colored("\nLetters Guessed: %s\n" % letters_guessed, 'red'))


            # Case 2: if the player enters a full word.
            elif len(guess) == len(random_word):
                if guess == random_word:
                    print(colored(picture[1], 'green'))
                    print("\nCongratulations! the word is \"%s\"" % random_word)
                    print(Score(level_selection, name))
                    guessed = True

                else:
                    # E.g.: The word is bowling but he/she enters'bowllng'.
                    print(colored("\nSomething is not part of the word, try again.\n", 'yellow'))


            # Case 3: if the player enters a full word but it's not the exact word. More of less letters.
            # E.g.: The word is bowling but he/she enters 'bowl' or 'bo' or 'bowlingg'.
            # They should enter 'bowling' or only one letter each turn.
            else:
                print("\n\"%s\" lenght does not equal to \"%s\" letters, try another!\n" % (guess,len(random_word)))


            status = ''
            if guessed == False:
                for letter in random_word:
                    if letter in letters_guessed:
                        status += letter
                    else:
                        status += ' _'
                print(colored(status, 'green'))

            if status == random_word:
                print(colored(picture[1], 'green'))
                print("\nCongratulations! the word is \"%s\"" % random_word)
                print(Score(level_selection, name))
                guessed = True

            elif tries == 0:
                print(colored(picture[0], 'red'))
                print("\nOh no! You have run out of guesses, better luck next time! The word is \"%s\"" % random_word)

    play_again()



if __name__ == '__main__':
    main()

