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

def color_stats(df):
    """Displays statistics about each color and color combination."""

    print('\nCalculating the win percentage of each color and color combination...\n')

    for color in color_identity_of_commander:
        wins = player_won.count('Yes')
        total_games = player_won.count()
        win_percentage = wins/total_games * 100

        print('{}: {}%'.format(color, win_percentage))

def main():
    while True:
        df = pd.read_csv('commander_data.csv')
        get_filters()
        color_stats(df)
        break

if __name__ == "__main__":
	main()