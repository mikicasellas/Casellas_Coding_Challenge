import random
from random import choice
from PIL import Image
import os


# getting working directory
cwd = os.getcwd()
os.chdir(cwd)
random.seed()

# setting word list & while condition
my_list = ['apples', 'oranges', 'pears', 'peaches', 'grapes',
           'pineapples', 'grapefruits', 'cherrys', 'strawberrys', 'kiwis']
playAgain = 'y'

while playAgain == 'y':

    # setting holding & display variables
    word = choice(my_list)
    list = ['_'] * len(word)
    list2 = []
    checker = word
    wrongGuess = 0
    correctGuess = 0
    game = 'ongoing'

    print('Welcome to Hangman!')
    print('The word has ' + str(len(word)) + ' letters.')

    # guess loop
    while game == 'ongoing':
        x = input('guess a letter')

        # if letter is not in word
        if word.find(x) != -1:
            print('it is in the word')
            index = word.index(x)
            list[index] = x
            print(list)
            word = word.replace(x, '!', 1)
            checker = checker.replace(x, '', 1)
            correctGuess = correctGuess + 1

        # if letter is in word
        else:
            print('incorrect guess')
            wrongGuess = wrongGuess + 1
            image = Image.open('Stage' + str(wrongGuess) + '.png')
            image.show()
            list2.append(x)
            print(list2)

            # validating lose condition
            if wrongGuess == 7:
                print('You Lost!')
                break

        # validating win condition
        if len(checker) == 0:
            game = 'end'
            print('You Win!')

    # end & loop condition
    print('Number of wrong guesses: ' + str(wrongGuess))
    print('Number of correct guesses: ' + str(correctGuess))
    playAgain = input('Press y to play again or any key to quit')

print('Thanks for playing!')
