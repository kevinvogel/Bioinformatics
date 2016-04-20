"""This function will calculate the GC% content of the given DNA sequence."""

# Filename: /Users/kevinvogel/PycharmProjects/git_projects_bioinformatics/gc_content.py

__author__ = 'Kevin Vogel'
__email__ = 'kevinvogel@mac.com'


def gc_function():
    """
    This function will calculate the GC% content of your desired sequence.
    :return: GC percentage to the hundredth decimal place
    """
    # Randomly inserted DNA sequence.
    seq = 'AAGCTCCTAATCACCCTCATAGCCTATAGTGATTCTCGACCTCGGTCAACTCTGCACGGCTTACAGGTAGGCCAGTTGACTAACTGTGGAGAATA'
    # Calculates the GC content of the DNA sequence.
    gc_content = ((seq.count('G') + seq.count('C')) / len(seq)) * 100
    # Prints the percentage to the console.
    print('The GC percentage of this sequence is: ' + str(round(gc_content, 2)) + '%.')


if __name__ == '__main__':
    print(gc_function())
