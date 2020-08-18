import time
import pandas as pd
import numpy as np

def color_stats(df):
    """Displays statistics about each color and color combination."""

    check = input('\nWould you like to see statistics based on color? y or n?\n').lower()
    while check != 'y' and check != 'n':
        check = input('\nPlease type y or n.\n').lower()
    if check == 'y':
        start_time = time.time()
        colors = ['W', 'U', 'B', 'R', 'G', 'WU', 'WB', 'WR', 'WG', 'UB', 'UR', 'UG', 'BR',
                  'BG', 'RG', 'WUB', 'WUR', 'WUG', 'WBR', 'WBG', 'WRG', 'UBR', 'UBG', 'URG',
                  'BRG', 'WUBR', 'WUBG', 'WURG', 'WBRG', 'UBRG', 'WUBRG', '0']

        one_color_wins = []
        two_color_wins = []
        three_color_wins = []
        four_color_wins = []
        five_color_wins = []
        one_color_games = []
        two_color_games = []
        three_color_games = []
        four_color_games = []
        five_color_games = []

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
                print(color + '\nWin percentage: ' + str(win_percentage) + '%\nMost common deck archetype: ' +
                      df['Deck Type'].mode()[0] + '\nMost common commander: ' + df['Commander'].mode()[0] + '\n')

                if color != '0' and len(color) == 1:
                    one_color_wins.append(wins)
                    one_color_games.append(total_games)
                elif len(color) == 2:
                    two_color_wins.append(wins)
                    two_color_games.append(total_games)
                elif len(color) == 3:
                    three_color_wins.append(wins)
                    three_color_games.append(total_games)
                elif len(color) == 4:
                    four_color_wins.append(wins)
                    four_color_games.append(total_games)
                elif len(color) == 5:
                    five_color_wins.append(wins)
                    five_color_games.append(total_games)


        print('Win percentage by number of colors:\nOne: ' + str(round(sum(one_color_wins) / sum(one_color_games) *
              100)) + '\nTwo: ' + str(round(sum(two_color_wins) / sum(two_color_games) * 100)) + '\nThree: ' +
              str(round(sum(three_color_wins) / sum(three_color_games) * 100)) + '\nFour: ' +
              str(round(sum(four_color_wins) / sum(four_color_games) * 100)) + '\nFive: ' +
              str(round(sum(five_color_wins) / sum(five_color_games) * 100)) + '\nColorless: ' + str(win_percentage))


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)

def main():
    while True:
        df = pd.read_csv('commander_data.csv')
        color_stats(df)
        break

if __name__ == "__main__":
	main()