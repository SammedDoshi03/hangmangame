import random
from words import list_of_words

# Getting Random Value(Word) From File(dist.py) and Converting(Returning) into Upper Format
def get_random_world():
    word = random.choice(list_of_words)
    #print('Selected word is ',word)
    return word.upper()

# Actual Game
def start_game(word):
   word_completion = '_' * len(word) 
   already_guesses_word = []
   already_guesses_letter = []
   chances = 6
   guessed = False
   print('Start let Start Game \n')
   print('Fill ', word_completion, ',Letters in Word:',len(word))
   while not guessed and chances > 0:
        guess = input(f'You have: ${chances} ,Enter a letter  or Word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in already_guesses_letter:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                chances -= 1
                already_guesses_letter.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                already_guesses_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in already_guesses_word:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                chances -= 1
                already_guesses_word.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(chances))
        #print(display_hangman_starting_from_body(chances))
        print('Word: ',word_completion)
        #print("\n")
   if guessed:
        print("Congrats, you guessed the word! You win!")
        #print(display_hangman_starting_from_body(6))
   else:
        print("Sorry, you ran out of chances. The word was " + word + ". Maybe next time!")


# Dispay HangMan hanging
def display_hangman(chances):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

# Dispay HangMan hanging V2.0
def display_hangman_starting_from_body(chances):
    stages = [  # final state: hanged Man to Death 
                """
                   --------
                   |      |
                   |      0
                   |     \\|/
                   |      |
                   |     / \\
                   -    
                """,
                #"hanged Man to Death (Without asking Last Wish)"
                
                # Fifth State With Hanging a Man Pillor , Upper Layer, Rop and Man
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Forth State With Pillor , Upper Layer and Man
                """
                   --------
                   |      
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Third State With Pillor With Man
                """
                   
                   |      
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Second state with Half Pillor With Man
                """
                   
                          
                          O
                         \\|/
                          |
                         / \\
                   -
                """,
                # initial empty state With Man
                """
                   
                          
                          O
                          |
                          |
                         / \\
                   -    
                """,
                
                # initial empty state With Man without Hands and legs
                """
                   
                          
                          O
                          |
                          |
                         
                   -    
                """,
                #Saved State
                #  """
                #   "Congrats, You Saved Man"
                #          
                #           O
                #          \\|/
                #           |
                #          / \\
                #    --           --   
                #    THANK YOU FOR PLAYING
                # """,
    ]
    return stages[chances]


# Initilaliaztion of Game
   # taking Word From File 
word = get_random_world()
   # passing word to Start game
start_game(word)
   # Play Again
while input("Play Again (Y/N)").upper() ==  "Y":
    word = get_random_world()
    start_game(word)