#!/usr/bin/env python
"""Challenge 19

   You are given the following information, but you may prefer to do some
   research for yourself.

     • 1 Jan 1900 was a Monday.
     • Thirty days has September,
       April, June and November.
       All the rest have thirty-one,
       Saving February alone,
       Which has twenty-eight, rain or shine.
       And on leap years, twenty-nine.
     • A leap year occurs on any year evenly divisible by 4, but not on a
       century unless it is divisible by 400.

   How many Sundays fell on the first of the month during the twentieth
   century (1 Jan 1901 to 31 Dec 2000)?
"""

def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
      return True
  return False

months = {
    'j':31,
    'f':28,
    'm':31,
    'a':30,
    'j':30,
    'y':31,
    'a':31,
    's':30,
    'o':31,
    'n':30,
    'd':31
}

for y in range(1900, 2001):
  extra_day = 0
  if is_leap_year(y):
    extra_day = 1




