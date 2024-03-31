import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    DNA_data = []
    filename = sys.argv[1]
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            DNA_data.append(row)
    # print(DNA_data)

    # TODO: Read DNA sequence file into a variable
    DNA_sq = []
    filename = sys.argv[2]
    with open(filename, "r") as file:
        DNA_sq = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    # Extract keys STR for use in function
    STR_keys = list(DNA_data[0].keys())[1:]
    # print(STR_keys)
    Find_Long = {}
    for i in STR_keys:
        Find_Long[i] = longest_match(DNA_sq, i)
        # Find_Long = longest_match(DNA_sq, "TATC")
    # print(Find_Long)

    # TODO: Check database for matching profiles
    # Loop in database
    for name in DNA_data:
        STR_match_Count = 0
        # Loop in each STR with Key
        for j in STR_keys:
            if int(name[j]) == Find_Long[j]:
                STR_match_Count = STR_match_Count + 1

        if STR_match_Count == len(Find_Long):
            print(name["name"])
            return

    print("No match")
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


main()
