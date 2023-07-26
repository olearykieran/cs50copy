import re


def main():
    # get card num from user
    cc_number = get_card()
    dig_length = len(cc_number)

    # Run card number through checks
    amex = isValidAmex(cc_number, dig_length)
    master = isValidMaster(cc_number, dig_length)
    visa = isValidVisa(cc_number, dig_length)
    
    # Run card though secret formula
    sum_every_other_digit = sum_of_alternate_digits(cc_number)

    # Check the last digit of the card and return card type if applicable
    if sum_every_other_digit % 10 != 0:
        print("INVALID")
    elif amex == True:
        print("AMEX")
    elif master == True:
        print("MASTERCARD")
    elif visa == True:
        print("VISA")
    else:
        print("INVALID")


# Check if card number is an Amex card
def isValidAmex(num, len):
    first_two_dig = num[0] + num[1]
    if len == 15 and (first_two_dig == '34' or first_two_dig == '37'):
        return True
    else:
        return False


# Check if card number is a Master card
def isValidMaster(num, len):
    first_two_dig = num[0] + num[1]
    if len == 16 and 50 <= int(first_two_dig) < 56:
        return True
    else:
        return False


# Check if card number is a Visa card
def isValidVisa(num, len):
    first_dig = num[0]
    if (len == 16 or len == 13) and first_dig == '4':
        return True
    else:
        return False


# Formula for getting the sum of every other digit from the 2nd to last number of the credit card
def sum_of_alternate_digits(num):
    total = 0
    for i in range(len(num) - 2, -1, -2):
        digit = int(num[i]) * 2
        if digit > 9:
            digit = sum(int(d) for d in str(digit))
        total += digit
    for i in range(len(num) - 1, -1, -2):
        total += int(num[i])
    return total


# Prompt user for card info
def get_card():
    while True:
        card = int(input("What is your Credit Card number? "))
        if card > 0:
            return str(card)


main()