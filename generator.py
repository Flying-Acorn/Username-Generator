import os
import random


def generate_username():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    # get user input
    num = 1
    # read word lists
    with open(os.path.join(__location__, 'nouns.txt')) as infile:
        nouns = infile.read().strip(' \n').split('\n')
    with open(os.path.join(__location__, 'adjectives.txt')) as infile:
        adjectives = infile.read().strip(' \n').split('\n')
    # read censor list
    with open(os.path.join(__location__, 'blacklist.txt')) as inline:
        censored = inline.read().strip(' \n').split('\n')
    # generate usernames
    for i in range(num):

        # construct username
        word1 = random.choice(adjectives)
        word2 = random.choice(nouns)
        # check if word2 is censored
        if word2 in censored:
            i -= 1
            continue
        # else make and print the username
        word1 = word1.title()
        word2 = word2.title()
        username = '{}{}{}'.format(word1, word2, random.randint(1, 99))

        # success
        return username
