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

def main():

    letters_guessed = []
    guessed = False

    # The player has 10 tries at the beginning of the game. 
    tries = 10

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
                guessed = True

            elif tries == 0:
                print(picture[0])
                print("\nOh no! You have run out of guesses, better luck next time! The word is \"%s\"" % random_word)


if __name__ == '__main__':
    main()