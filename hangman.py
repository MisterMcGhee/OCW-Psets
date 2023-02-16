import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = infile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    if all(letter in letters_guessed for letter in secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            guessed_word.append("_")

    return("".join(guessed_word))


def get_available_letters(letters_guessed):
    available_letters = list(string.ascii_lowercase)

    for letter in letters_guessed:
        if letter in available_letters:
            available_letters.remove(letter)
    return (available_letters)

def hangman(secret_word):
    num_guesses = 6
    letters_guessed = []
    secret_word_length = len(secret_word)
    # Give the user starting text before we begin the while loop
    print("Welcome to Hangman! The secret word contains " + str(secret_word_length) + " letters.")
    print("You start with " + str(num_guesses) + " guesses")
    # Start of the game.
    while num_guesses > 0:
        print("Your available letters are " + str(get_available_letters(letters_guessed)) + ".")
# Get user input for guessed letter. No validation yet
        guessed_letter = input("What letter would you like to guess?")
# Print an empty line just to make the console prettier
        print("")
# Adds the guessed letter to the list of all previously guessed letters
        letters_guessed.extend(guessed_letter)
# Increments the number of remaining guesses if the guess is wrong
        if guessed_letter not in secret_word:
            print("Sorry. " + guessed_letter + " is not in the secret word:" + str(get_guessed_word(secret_word, letters_guessed)))
            num_guesses -= 1
        else:
            print("Good Guess!"  + str(get_guessed_word(secret_word, letters_guessed)))
# Tells the user how many guesses left regardless of correct or incorrect guess.
        print("You have " + str(num_guesses) + " guesses left.")
# Win condition for the game.
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("You win!")
            break
# Lose condition of the game.
    else:
        print("Sorry. You lose. The secret word was " + secret_word)







def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    secret_word = "cup"
    # secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
