import time
import pandas as pd
import numpy as np
import scipy.stats as ss

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

        white_wins = []
        blue_wins = []
        black_wins = []
        red_wins = []
        green_wins = []
        white_games = []
        blue_games = []
        black_games = []
        red_games = []
        green_games = []

        def binom_prob(games, successes):
            hh = ss.binom(games, .25)

            p = 0
            for k in range(1, successes + 1):
                p += hh.pmf(k)
            return p

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
                win_percentage = round(wins/total_games * 100, 1)

                #Test for statistcal significance.
                total_p = binom_prob(total_games, wins)

                if round(total_p) < .05:
                    print(color, '\nWin percentage: ', win_percentage, '%\nMost common deck archetype: ',
                          df['Deck Type'].mode()[0], '\nMost common commander: ', df['Commander'].mode()[0],
                          '\nThis win rate is statistcally significant.\n')
                else:
                    print(color, '\nMost common deck archetype: ', df['Deck Type'].mode()[0],
                          '\nMost common commander: ', df['Commander'].mode()[0],
                          '\nNo statistically significant win rate data for this color combination.\n')

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

                #Determine how well each color did even as part of a combination.
                if 'W' in color:
                    white_wins.append(wins)
                    white_games.append(total_games)
                if 'U' in color:
                    blue_wins.append(wins)
                    blue_games.append(total_games)
                if 'B' in color:
                    black_wins.append(wins)
                    black_games.append(total_games)
                if 'R' in color:
                    red_wins.append(wins)
                    red_games.append(total_games)
                if 'G' in color:
                    green_wins.append(wins)
                    green_games.append(total_games)

        one_color_p = binom_prob(sum(one_color_games), sum(one_color_wins))
        two_color_p = binom_prob(sum(two_color_games), sum(two_color_wins))
        three_color_p = binom_prob(sum(three_color_games), sum(three_color_wins))
        four_color_p = binom_prob(sum(four_color_games), sum(four_color_wins))
        five_color_p = binom_prob(sum(five_color_games), sum(five_color_wins))

        white_p = binom_prob(sum(white_games), sum(white_wins))
        blue_p = binom_prob(sum(blue_games), sum(blue_wins))
        black_p = binom_prob(sum(black_games), sum(black_wins))
        red_p = binom_prob(sum(red_games), sum(red_wins))
        green_p = binom_prob(sum(green_games), sum(green_wins))

        print('Win percentage by number of colors:\nOne:', round(sum(one_color_wins) / sum(one_color_games) * 100, 1),
              '% p =', round(one_color_p, 3), '\nTwo:', round(sum(two_color_wins) / sum(two_color_games) * 100, 1),
              '% p =', round(two_color_p, 3), '\nThree:', round(sum(three_color_wins) / sum(three_color_games) * 100,
              1), '% p =', round(three_color_p, 3), '\nFour:', round(sum(four_color_wins) / sum(four_color_games)
              * 100, 1), '% p =', round(four_color_p, 3), '\nFive:', round(sum(five_color_wins)
              / sum(five_color_games) * 100, 1), '% p =', round(five_color_p, 3), '\nColorless:', win_percentage,
              '% p =', round(total_p, 3))

        print('\nWin percentage by color (mono or in a combination):\nWhite:', round(sum(white_wins) / sum(white_games)
              * 100, 1), '% p =', round(white_p, 3), '\nBlue:', round(sum(blue_wins) / sum(blue_games) * 100, 1),
              '% p =', round(blue_p, 3), '\nBlack:', round(sum(black_wins) / sum(black_games) * 100, 1), '% p =',
              round(black_p, 3), '\nRed:', round(sum(red_wins) / sum(red_games) * 100, 1), '% p =', round(red_p, 3),
              '\nGreen:', round(sum(green_wins) / sum(green_games) * 100, 1), '% p =', round(green_p, 3),
              '\nColorless:', win_percentage, '% p =', round(total_p, 3)) 


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)

def main():
    while True:
        df = pd.read_csv('commander_data.csv')
        color_stats(df)
        break

if __name__ == "__main__":
	main()