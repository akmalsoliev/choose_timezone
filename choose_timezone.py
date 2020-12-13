# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz
import random

given_timezones = []
for names in range(1, 11):
    given_timezones.append(pytz.all_timezones[random.randint(1, len(pytz.all_timezones))])

print('Hello and welcome to this small timezone checker application. Your options are:')

for numbers in range(0, len(given_timezones)):
    print('{}. {}'.format(numbers+1, given_timezones[numbers]))

while True:
    user_input = input('''Please choose the timezone you'd like to see.\n''')
    try:
        if 10 >= int(user_input) >= 1:
            user_input = int(user_input) - 1
            chosen_timezone = pytz.timezone(given_timezones[user_input])
            wanted_timezone = datetime.datetime.now(tz=chosen_timezone)
            print('''Current time at: {} is {}:{}\nThe date is: {} of {}, {}'''.format(chosen_timezone, wanted_timezone.hour, wanted_timezone.minute, wanted_timezone.day, wanted_timezone.month, wanted_timezone.year))
            break
        else:
            print("The following option is not available. Please choose from 1 to {}".format(len(given_timezones)))
    except:
        print("The following option is not available. Please choose from 1 to {}".format(len(given_timezones)))