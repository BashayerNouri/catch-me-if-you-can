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
        self.word = len(random_word) 
        self.bonus = 5
        self.name = name

    def get_score(self):
        if self.level_selection == 1:
            return (self.level_selection) * (10 + self.word + self.bonus)
        elif self.level_selection == 2:
            return (self.level_selection) * (20 + self.word + self.bonus)
        else:
            return (self.level_selection) * (30 + self.word + self.bonus)

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
    for messsage in messsages:
        print (messsage)
        time.sleep(1.3)

def play_again():
    print("\nWould you like to play again?")
    time.sleep(1)

    while True:
        answer = input("If yes enter \"yes\" or \"y\". If no enter \"no\" or \"n\" ").lower()
        if answer == "y" or answer == "yes":
            main()
        elif answer == "n" or answer == "no":
        	print("\nGoodbye. See you next time!")
        	break
        else:
            print("Please enter \"yes\" or \"y\". \"no\" or \"n\" ")
            time.sleep(1)

def main():

    level = { 
    "easy": 10,
    "intermediate": 6,
    "difficult":  2,
    }

    selection = False
    letters_guessed = []
    guessed = False
    

    print("\nThere are multiple difficulty settings shown below:")
    time.sleep(1)
    print("\t1. Easy (10 attempts)")
    time.sleep(1)
    print("\t2. Intermediate (6 attempts)")
    time.sleep(1)
    print("\t3. Difficult (2 attempts)")
    time.sleep(1)

    while selection == False:
        level_selection = input("\nSelect A Level: ")
        try:
            level_selection = int(level_selection)
            if level_selection == 1:
                tries = level['easy']
                selection = True
            elif level_selection == 2:
                tries = level['intermediate']
                selection = True
            elif level_selection == 3:
                 tries = level['difficult']
                 selection = True
            else:
                print("Please select a number from 1 to 3...")
        except ValueError:
                print("You didn't enter a number!")
    
    name = input("\nEnter a name, nickname or team name: ")
    
    weclcome_message()

    print("\nThe word contains", len(random_word), 'letters. \n')
    print(len(random_word) * (" _"))
    
    while guessed == False and tries > 0:
            print("\nYou have %s tries." % tries)
            guess = input("\nEnter one letter or the full word: ").lower()

            if len(guess) == 1:
                if not guess.isalpha():
                    print("\n\'%s\' is not a letter, enter a letter!\n" % guess)
                    print("\nLetters Guessed: %s\n" % letters_guessed)

                elif guess in letters_guessed:
                    print("\n\'%s\' has been guessed before, try another letter.\n" % guess)
                    print("\nLetters Guessed: %s\n" % letters_guessed)

                elif guess not in random_word:
                    print("\n\'%s\' is not part of the word, try another letter.\n" % guess)
                    letters_guessed.append(guess)
                    tries -=1
                    print("\nLetters Guessed: %s\n" % letters_guessed)

                elif guess in random_word:
                    print("\nWell done, that letter exists in the word!\n")
                    letters_guessed.append(guess)
                    print("\nLetters Guessed: %s\n" % letters_guessed)

            elif len(guess) == len(random_word):
                if guess == random_word:
                    print(picture[1])
                    print("\nCongratulations! the word is \"%s\"" % random_word)
                    print(Score(level_selection, name))
                    guessed = True

                else:
                    print("\nSomething is not part of the word, try again.\n")
                    tries -=1

            else:
                print("\n\"%s\" lenght does not equal to \"%s\" letters, try another!\n" % (guess,len(random_word)))


            status = ''
            if guessed == False:
                for letter in random_word:
                    if letter in letters_guessed:
                        status += letter
                    else:
                        status += ' _'
                print(status)

            if status == random_word:
                print(picture[1])
                print("\nCongratulations! the word is \"%s\"" % random_word)
                print(Score(level_selection, name))
                guessed = True

            elif tries == 0:
                print(picture[0])
                print("\nOh no! You have run out of guesses, better luck next time! The word is \"%s\"" % random_word)

    play_again()

if __name__ == '__main__':
    main()