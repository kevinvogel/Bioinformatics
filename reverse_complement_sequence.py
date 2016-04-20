"""This function will display the reverse complement of the given DNA sequence."""

# Filename: /Users/kevinvogel/PycharmProjects/git_projects_bioinformatics/reverse_complement_sequence.py

__author__ = 'Kevin Vogel'
__email__ = 'kevinvogel@mac.com'


def reverse_complement(seq):
    """
    This function will display the reverse complement of a DNA sequence.
    :return: reverse complement of the DNA sequence
    """
    # Dictionary to store the base pairs.
    seq_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}
    # Replaces each nucleotide with its base pair partner and reverses the sequence.
    return "".join([seq_dict[base] for base in reversed(seq)])


if __name__ == '__main__':
    print(reverse_complement(seq))
