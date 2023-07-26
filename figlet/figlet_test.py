#!/usr/bin/env python
import random
from pyfiglet import Figlet
import argparse
from sys import exit

parser = argparse.ArgumentParser(description='ASCII Art Generator')
parser.add_argument('-f', '--font', help='Specify the font to use')
args = parser.parse_args()

fig = Figlet()

if args.font is None:
    fig.setFont(ran_font=random.choice(fig.getFonts()))
else:
    fig.setFont(font=args.font)

user_input = input("Input: ")
print(fig.renderText(user_input))