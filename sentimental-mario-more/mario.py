# Creates a reflection of blocks x high
def main():
    height = get_height()
    for c in range(height):
        for s in range(c, height - 1):
            print(" ", end='')
        for i in range(c + 1):
            print("#", end='')
        print("  ", end='')
        for j in range(c + 1):
            print("#", end='')
        print()


# Asks user to set a height
def get_height():
    while True:
        blocks = input("How many blocks high? ")
        if blocks.isdigit():
            blocks = int(blocks)
            if blocks >= 1 and blocks <= 8:
                return blocks


# Call main
main()
