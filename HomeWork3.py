import random
from functools import reduce
import functools


def openWords(file):
    words = open(file, "r")
    return words


def getWordLength():
    wordLength = int(input("May you write count of letters in your word please ? "))

    return wordLength

def attemptCount(attemt):
    return attemt

def printLines():
    len = getWordLength()
    wordArea = ['_' for letter in range(len)]
    return wordArea

def letterPresent(letter):
    char = input("PC: Is there a letter '%s' in a word? (Y / N) " % (letter))
    if char == 'Y':
        print("Nice,I knew that this letter is present!", '\n')
    elif char == 'N':
        print("Oh let me try again", '\n')



def startApp(file):
    words = openWords(file)
    wordArea = printLines()
    count = 0;
    win = False
    while not win:
        #TODO
        print(wordArea)
        letter = chr(random.randrange(97, 97 + 26 + 1))
        letterPresent(letter)

startApp("words.txt")
