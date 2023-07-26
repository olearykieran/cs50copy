import re


def main():
    # Ask user for input
    text = input("Text: ")

    # Get letter and word count
    letters = letter_count(text)
    words = len(text.split())
    sentence = get_sent(text)

    # Run input through secret formula
    count = secret_formula(letters, words, sentence)

    # Prints grade level
    answer(count)


# Return sentence count
def get_sent(text):
    t = 0
    for i in text:
        if i in [".", "!", "?"]:
            t += 1
    return t


# Return letter count
def letter_count(text):
    count = 0
    for i in text:
        if i.isalpha():
            count += 1
    return count


# Run through formula
def secret_formula(let, wor, sen):
    l = let / wor * 100
    s = sen / wor * 100
    formula = 0.0588 * l - 0.296 * s - 15.8
    rounded = round(formula)
    return rounded


# Print results
def answer(count):
    grade = 0
    if count <= 1:
        print("Before Grade 1")
    elif count >= 16:
        print("Grade 16+")
    else:
        print("Grade {}" .format(count))


main()