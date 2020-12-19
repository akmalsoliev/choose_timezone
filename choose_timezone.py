import datetime
import pytz
import random

number_of_inputs = 10
random_number = list(random.sample(range(0, len(pytz.all_timezones)), number_of_inputs))
print(random_number)

print('Hello and welcome to this small timezone checker application. Your options are:')
print('''0. Exit''')

for numbers in range(0,number_of_inputs):
    print('{}. {}'.format(numbers+1, pytz.all_timezones[random_number[numbers]]))

while True:
    user_input = input('''Please choose the timezone you'd like to see.\n''')
    try:
        user_input=int(user_input)
        if 10 >= user_input >= 1:
            user_input =- 1
            index = random_number[user_input] #if 1 = 0 
            print(index)
            time_zone_name = pytz.all_timezones[index]

            chosen_timezone = pytz.timezone(time_zone_name)
            wanted_timezone = datetime.datetime.now(tz=chosen_timezone)
            print('Current time at: {} is {}:{}'.format(chosen_timezone, wanted_timezone.hour, wanted_timezone.minute))
            print('The date is: {} of {}, {}'.format(wanted_timezone.day, wanted_timezone.month, wanted_timezone.year))
            break

        elif user_input == 0:
            break

        else:
            print("The following option is not available. Please choose from 1 to {}".format(number_of_inputs))

    except:
        print("The following option is not available. Please choose from 1 to {}".format(number_of_inputs))