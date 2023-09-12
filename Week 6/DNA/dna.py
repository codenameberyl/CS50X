import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    database_file = sys.argv[1]
    database = read_database(database_file)

    # Read DNA sequence file into a variable
    sequence_file = sys.argv[2]
    sequence = read_sequence(sequence_file)

    # Find longest match of each STR in DNA sequence
    counts = {}
    for key in database[0][1:]:
        counts[key] = longest_match(sequence, key)

    # Check database for matching profiles
    match = find_match(database, counts)
    if match:
        print(match)
    else:
        print("No match")


def read_database(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        database = [row for row in reader]
    return database


def read_sequence(filename):
    with open(filename, "r") as file:
        sequence = file.read()
    return sequence


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


def find_match(database, counts):
    for row in database[1:]:
        match = True
        for i in range(1, len(row)):
            if int(row[i]) != counts[database[0][i]]:
                match = False
                break
        if match:
            return row[0]
    return None


if __name__ == "__main__":
    main()
