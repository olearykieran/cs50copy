#!/usr/bin/env python
import sys
import random
from pyfiglet import Figlet
from sys import exit

arg = sys.argv
fig = Figlet()
fig.getFonts()


if len(arg) == 2 or len(arg) > 3:
    print("Usage: no command line args or 'program.py -f font'")
    exit(1)

if len(arg) == 3:
    if arg[1] != "-f" and arg[1] != "--font":
        print("Invalid 2nd argument")
        exit(1)
    elif arg[2] not in fig.getFonts():
        print("Invalid 3rd argument")
        exit(1)

user_input = input("Input: ")

if len(arg) == 1:
    fig.setFont(font=random.choice(fig.getFonts()))
    print(fig.renderText(user_input))

else:
    fig.setFont(font=arg[2])
    print(fig.renderText(user_input))




