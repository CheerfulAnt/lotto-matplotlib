#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name:  lotto.py
# Description:  The script processes the file lottery_draws.txt with the results
#               of the lottery game (6 of 49) from 27/01/1957 to 31/03/2022.
#               The script displays the date, whether the year is a leap year,
#               the sum of the date digits, Numerology Life Path Number
#               (if number is a Master Number (11, 22, 33, 44, 55) will stop
#               count). It also displays the numbers of the drawn balls,
#               their sum, average, median, number of prime numbers, and
#               frequency of occurrence of numbers in all draws
#               together with charts.
# Author: CheerfulAnt@outlook.com
# Version: 1.0
# Date: 15 July 2022 - 15:00 (UTC+02:00)


from datetime import datetime
import matplotlib.pyplot as plt
import lotto_functions as lofu

number_of_balls = 6

date_format_from_file = '%d.%m.%Y'

numbers_frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0,
                     10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0,
                     18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0,
                     26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0,
                     34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0,
                     42: 0, 43: 0, 44: 0, 45: 0, 46: 0, 47: 0, 48: 0, 49: 0}

print('\n', '{:^10} {:^7} {:^6} {:^5} {:^23} {:^8} {:^8} {:^10} {:^6}'
      .format('Date', 'Leap', 'D_Sum', 'Mst', 'Balls', 'Sum', 'Average',
              'Median', 'Prime'), end='\n\n')

try:
    with open('draws.txt', 'r', encoding='utf8') as file:
        for line in file:
            # strip whitespaces in the line
            line = line.strip()
            draws_data = line.split(' ')
            # delete first column with unnecessary line numbers
            del draws_data[0]
            # convert date to YYYY-MM-DD from DD.MM.YYYY
            draws_data[0] = str(datetime.strptime(draws_data[0],
                                date_format_from_file).date())
            draws_data[1] = draws_data[1].split(',')
            # convert all items in list to int
            draws_data[1] = [int(item) for item in draws_data[1]]
            # append numbers sum
            draws_data.append(sum(draws_data[1]))
            # append average
            draws_data.append(sum(draws_data[1]) / number_of_balls)
            # append median
            draws_data.append(lofu.median(draws_data[1]))
            # append is leap year
            draws_data.insert(1, lofu.leap_year(int(draws_data[0][:4])))
            # insert the sum of the digits of the date
            draws_data.insert(2, lofu.draw_date_sum(draws_data[0]))
            # insert birth number or master number (numerology)
            draws_data.insert(3, lofu.master(draws_data[0],
                                             lofu.draw_date_sum))
            # append quantity of the prime numbers
            draws_data.append(lofu.prime_counter(draws_data[4], lofu.prime))

            for item in draws_data[4]:
                num_freq = numbers_frequency.get(item)
                numbers_frequency.update({item: num_freq + 1})

            print('{:<11} {:<2} {:<2} {:<2} {:>3} {:<2} {:>2} {:<2} {:>2}'
                  '{:>3} {:>3} {:>3} {:>3} {:>3} {:>2} {:>3} {:<2} {:>2,.3f}'
                  '{:>2} {:>8,.3f} {:>2} {:< 5}'
                  .format(draws_data[0], '|', draws_data[1], '|',
                          draws_data[2], '|', draws_data[3], '|',
                          *draws_data[4], '|', draws_data[5], '|',
                          draws_data[6], '|', draws_data[7], '|',
                          draws_data[8]))

except FileNotFoundError:
    print("File with draws not found.")
except:
    print("Unknown error :-)")

print('\n', 'Numbers frequency: ', end='')

new_line = 0

for key, value in numbers_frequency.items():

    if not new_line % 10:

        print('\n')

    print('{} {:<2} {} {} {:<4}'
          .format('\033[31m', key, '\033[0m', ':', value), end='')

    new_line += 1

print()

# ----- plots -----

def value_label(balls_in, values_in, axs_index):

    font = {'size': 9,
            'color': 'white'}

    for i in range(len(values_in)):
        axs[axs_index].text(i, 150, '\n'.join(str(values_in[i])),
                            ha='center', va='center', **font)

balls = list(numbers_frequency.keys())
values = list(numbers_frequency.values())

numbers_frequency_sorted = sorted(numbers_frequency.items(),
                                  key=lambda x: x[1], reverse=True)

numbers_frequency_sorted = dict((x, y) for x, y in numbers_frequency_sorted)

balls_sorted = list(numbers_frequency_sorted.keys())
values_sorted = list(numbers_frequency_sorted.values())

fig, axs = plt.subplots(4, 1, figsize=(20, 10), dpi=200)

fig.suptitle('Frequency of occurrence of the numbers in lottery draws from '
             '27 January 1957 to 31 March 2022 (6707 draws).', fontsize=16)

value_label(balls, values, 0)
value_label(balls_sorted, values_sorted, 2)

axs[0].bar(range(len(values)), values, tick_label=balls, width=0.8)
axs[0].margins(0.015, 0.08)
axs[0].set_xlabel('Numbers of the balls.')
axs[0].set_ylabel('Quantity of the balls.')
axs[0].set_title('The frequency of the balls in the draws.', y=1.05)

balls.insert(0, 'Ball')
values.insert(0, 'Qty')

axs[1].axis('tight')
axs[1].axis('off')

table = axs[1].table(cellText=[values],
                     colLabels=balls,
                     cellLoc='center',
                     rowLoc='center',
                     loc='best',
                     bbox=(-0.01, 0.3, 1, 0.5))

table.scale(1, 2)

axs[2].bar(range(len(values_sorted)), values_sorted, tick_label=balls_sorted,
           width=0.8)
axs[2].margins(0.015, 0.08)
axs[2].set_xlabel('Numbers of the balls.')
axs[2].set_ylabel('Quantity of the balls.')
axs[2].set_title('The frequency of the balls in the draws in'
                 'descending order.', y=1.05)

balls_sorted.insert(0, 'Ball')
values_sorted.insert(0, 'Qty')

axs[3].axis('tight')
axs[3].axis('off')

table_sorted = axs[3].table(cellText=[values_sorted],
                            colLabels=balls_sorted,
                            cellLoc='center',
                            rowLoc='center',
                            loc='best',
                            bbox=(-0.01, 0.3, 1, 0.5))

table_sorted.scale(1, 2)

plt.show()
