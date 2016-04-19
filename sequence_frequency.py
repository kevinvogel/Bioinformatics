"""Given a FASTA file with DNA sequences, find 10 most frequent sequences and return the sequence
and their counts in the file."""

# Filename: /Users/kevinvogel/PycharmProjects/fasta_project/freq_of_seq.py

from Bio import SeqIO
from collections import Counter

__author__ = 'Kevin Vogel'
__email__ = 'kevinvogel@mac.com'


def freqfastaseq():
    """
    Stores file in an array and counts the 10 most frequent sequences.
    :return: sequence and count in the file
    """
    sequences = []
    fasta_sequences = SeqIO.parse(open('sample.fasta', 'r'), 'fasta')
    for fasta in fasta_sequences:
        sequence = str(fasta.seq)
        sequences.append(sequence)
    count = Counter(sequences)
    most_common_seq = count.most_common(10)
    return most_common_seq


print("Here are the 10 most frequent sequences and their counts in the .fasta file: ")

if __name__ == '__main__':
    print(freqfastaseq())
