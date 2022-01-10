# DNA

A program that reads a DNA sequence and a CSV file with the STR (a short sequence of unique, repeating DNA) information of several individuals and identifies to whom the DNA sequence belongs

# USAGE
Enter python dna.py followed by a csv file (data.csv) and a DNA sequence file (sequence.txt). 

Examples:

$ python dna.py databases/small.csv sequences/1.txt

Bob

$ python dna.py databases/small.csv sequences/2.txt

No match

$ python dna.py databases/small.csv sequences/4.txt

Alice

$ python dna.py databases/large.csv sequences/5.txt

Lavender

$ python dna.py databases/large.csv sequences/14.txt

Severus

$ python dna.py databases/large.csv sequences/17.txt

Harry
