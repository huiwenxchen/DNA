import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Incorrect command-line arguments")
        return 1

    # TODO: Read database file into a variable  
    # Open the database file
    file = open(sys.argv[1], "r")
    # Store the databse file in a dictionary
    reader = csv.DictReader(file)

    # TODO: Read DNA sequence file into a variable
    # Open the DNA sequence file
    DNA = open(sys.argv[2], "r")
    # Read the content into a variable
    sequence_content = DNA.read()

    # Initialize a dictionary of the sequence
    sequence_dict = {}

    # TODO: Find longest match of each STR in DNA sequence
    # Iterate through the subsequences in the csv header and calculate the longest count of each STR repeat
    for subsequence in reader.fieldnames[1:]:
        sequence_dict[subsequence] = longest_match(sequence_content, subsequence)

    # TODO: Check database for matching profiles
    # For each row, check if STR matches
    for row in reader:
        # Initialize a counter to keep track of and reset the number of matches for each individual
        Num_match = 0 
        # Iterate through each subsequence to check if the subsequence count has a match
        for subsequence in reader.fieldnames[1:]:
            if int(sequence_dict[subsequence]) == int(row[subsequence]):
                # Increase counter if match
                Num_match += 1
        # Print name if all of the STR repeats match
        if Num_match == len(reader.fieldnames[1:]):
            print(row['name']) 
            return
    # If no match is found
    print("No match")


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

# Jayden Personnat helped
