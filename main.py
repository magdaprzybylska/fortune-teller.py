import random

import fortunes
from fortunes import *

game = True

print(banner)

while game:

    day = int(input("Please insert your birthday: "))
    month = input("Please insert your birth month (e.g. march, july): ").lower()
    print("")

    if month == 'april' or month == 'june' or month == 'september' or month == 'november':
        if day > 30 or day < 0:
            print('Invalid input. ')
            break
    elif month == 'february':
        if day > 29 or day < 0:
            print('Invalid input. ')
            break
    else:
        if day > 31:
            print("Invalid input. ")
            break

    if month == 'december':
        astro_sign = 'sagittarius' if (day < 22) else 'capricorn'
    elif month == 'january':
        astro_sign = 'capricorn' if (day < 20) else 'aquarius'
    elif month == 'february':
        astro_sign = 'aquarius' if (day < 19) else 'pisces'
    elif month == 'march':
        astro_sign = 'pisces' if (day < 21) else 'aries'
    elif month == 'april':
        astro_sign = 'aries' if (day < 20) else 'taurus'
    elif month == 'may':
        astro_sign = 'taurus' if (day < 21) else 'gemini'
    elif month == 'june':
        astro_sign = 'gemini' if (day < 21) else 'cancer'
    elif month == 'july':
        astro_sign = 'cancer' if (day < 23) else 'leo'
    elif month == 'august':
        astro_sign = 'leo' if (day < 23) else 'virgo'
    elif month == 'september':
        astro_sign = 'virgo' if (day < 23) else 'libra'
    elif month == 'october':
        astro_sign = 'libra' if (day < 23) else 'scorpio'
    elif month == 'november':
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
    else:
        print("Invalid input. ")
        break

    random_fortunes = random.choice(fortunes[astro_sign])
    final_fortune = str(random_fortunes)

    print(f"Your astrological sign is: {astro_sign.title()}")
    print(f"Your fortune: {final_fortune}\n")
    should_continue = input("Do you want to draw another fortune? Type 'y' or 'n': ")

    if should_continue == "y":
        game = True
    elif should_continue == "n":
        game = False
    else:
        print("Invalid input. ")
        game = False

    print("_________________________________________________________________________\n")