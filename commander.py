import time
import pandas as pd
import numpy as np

def color_stats(df):
    """Displays statistics about each color and color combination."""

    print('\nCalculating the win percentage of each color and color combination...\n')
    start_time = time.time()
    colors = ['W', 'U', 'B', 'R', 'G', 'WU', 'WB', 'WR', 'WG', 'UB', 'UR', 'UG', 'BR',
              'BG', 'RG', 'WUB', 'WUR', 'WUG', 'WBR', 'WBG', 'WRG', 'UBR', 'UBG', 'URG',
              'BRG', 'WUBR', 'WUBG', 'WURG', 'WBRG', 'UBRG', 'C']

    for color in colors:
        df = pd.read_csv('commander_data.csv')
        df = df[df['Color Identity of Commander'] == color]
        if df.empty:
            print('There is no data for {}.'.format(color))
        else:
            wins = 0
            for record in df['Player Won']:
                if record == 'Yes':
                    wins += 1
            total_games = df['Player Won'].count()
            win_percentage = round(wins/total_games * 100)
            print('{}: {}%'.format(color, win_percentage))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def main():
    while True:
        df = pd.read_csv('commander_data.csv')
        color_stats(df)
        break

if __name__ == "__main__":
	main()