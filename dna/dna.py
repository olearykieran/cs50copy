import csv
import sys
import argparse


def main():

    # Check for command-line usage
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='1st Argument')
    parser.add_argument('arg2', help='2nd Argument')
    args = parser.parse_args()
    subject_csv = args.arg1
    dna_to_match = args.arg2

    # Read database file into a variable
    with open(subject_csv) as subjects:
        reader = csv.DictReader(subjects)
        dict = {}
        dict = reader
        new_keys = reader.fieldnames[1:]
        """ for row in reader:
            for k in new_keys:
                value = row[k] """

    # Read DNA sequence file into a variable
        with open(dna_to_match, 'r') as dna:
            dna_list = ()
            dna_list = dna.read()
        results = {}
    # Find longest match of each STR in DNA sequence
        for item in new_keys:
            results[item] = longest_match(dna_list, item)
    # Check database for matching profiles
        its_a_match(results, reader)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


# Check results of repeats vs original csv file
def its_a_match(results, reader):
    match_found = False
    for row in reader:
        match = True
        for key, value in results.items():
            if int(row.get(key)) != value:
                match = False
        if match:
            print(row['name'])
            match_found = True
    if not match_found:
        print('No match')


main()
