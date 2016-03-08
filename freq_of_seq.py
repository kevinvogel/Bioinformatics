from Bio import SeqIO
from collections import Counter

# Prompt user for desired .fasta file.
seq = input("Enter the .fasta sequence file you wish to work with: ")
file = open(seq, 'r')
line = file.read()
print(line)
print("\n")

# Function to parse and count the 10 most frequent sequences in the .fasta file.
def freqfastaseq(file):
    # Stores file in an array.
    sequences = []
    fasta_sequences = SeqIO.parse(open(file), 'fasta')
    for fasta in fasta_sequences:
        sequence = str(fasta.seq)
        sequences.append(sequence)
    # Counts the 10 most frequent sequences.
    count = Counter(sequences)
    most_common_seq = count.most_common(10)
    return most_common_seq

print("\n")
print("Here are the 10 most frequent sequences and their counts in the fasta file above: ")

# Prints sequences in a list.
for i in freqfastaseq(seq):
    print(i)
print("\n")
