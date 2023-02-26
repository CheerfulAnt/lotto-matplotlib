#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name: lotto_fonctions.py
# Description: Functions set for lotto.py

# Author: CheerfulAnt@outlook.com
# Version: 1.0
# Date: 15 July 2022 - 15:00 (UTC+02:00)

# sums digits from date YYYY-MM-DD (string)

def draw_date_sum(date_in):
    numbers_sum = 0

    for char in date_in:
        if char.isdigit():
            numbers_sum += int(char)
    return numbers_sum

# sums recursively digits until one digit is found, if it finds "master number"
# it returns them instead of the sum of all
# needs draw_date_sum() function

def master(date_in, draw_date_sum_in):
    master_number = ['11', '22', '33', '44', '55']

    if len(str(date_in)) > 1:

        date_in = str(draw_date_sum_in(date_in))

        if date_in in master_number:

            return int(date_in)
        else:
            return master(date_in, draw_date_sum_in)

    if len(str(date_in)) == 1:
        return int(date_in)

# returns True if year is leap, otherwise False,
# with no checking if year is before 1582

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    else:
        return 0

# returns median

def median(values, values_amount=6):
    if values_amount % 2 == 0:
        median = (values[int(values_amount / 2) - 1] +
                  (values[int(values_amount / 2)])) / 2
    else:
        median = values[int((values_amount + 1) / 2) - 1]
    return median

# prime number test

def prime(number_in):

    i = 2
    square_root_number = number_in**(1/2)

    if number_in == 1:
        return 0

    while i <= square_root_number:

        if not (number_in % i):
            return 0
        i += 1

    return 1

# prime numbers counter, needs prime() function

def prime_counter(numbers_list_in, prime_in):

    counter_in = 0

    for number_in in numbers_list_in:

        if prime_in(number_in):
            counter_in += 1

    return counter_in
