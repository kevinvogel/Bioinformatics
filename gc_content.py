"""This function will calculate the GC% content of the given DNA sequence."""

# Filename: /Users/kevinvogel/PycharmProjects/git_projects_bioinformatics/gc_content.py

__author__ = 'Kevin Vogel'
__email__ = 'kevinvogel@mac.com'


def gc_function(seq):
    """
    This function will calculate the GC% content of your desired sequence.
    :param seq:
    :return: GC percentage to the hundredth decimal place
    """
    # Calculates the GC content of the DNA sequence.
    gc_content = ((seq.count('G') + seq.count('C')) / len(seq)) * 100
    return gc_content


if __name__ == '__main__':
    gc_pct = (gc_function(seq='CGTAGATGATCGATGCATG'))
    print('The GC percentage of this sequence is: ' + str(round(gc_pct, 2)) + '%.')
