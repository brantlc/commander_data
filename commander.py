import pandas as pd
import numpy as np

def get_filters():
    """
    Asks user to specify if they want to see stats about winners or losers.

    :return: 
        (str) placing - place of player in final standings
    """

    print('Hello! Let\'s explore some Magic the Gathering Commander data!')
    placing = input('Do you want to see stats about winners or losers?\n').lower()

    while placing != 'winners' and placing != 'losers':
        placing = input('Please type winners or losers.\n').lower()

    print('-'*40)
    return placing

def main():
    while True:
        get_filters()
        break

if __name__ == "__main__":
	main()