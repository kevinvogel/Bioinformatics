# Recursively find all FASTQ files in a directory and report each file name and the percent of sequences in
# that file that are greater than 30 nucleotides long.

# !/usr/bin/python

import os
from Bio import SeqIO

__author__ = "Kevin Vogel"
__email__ = "kevinvogel@mac.com"


def directory_files():
    """
    # traverse root directory, list directories as dirs and files as files
    """
    for root, dirs, files in os.walk("."):
        path = root.split('/')
        print((len(path) - 1) * '\t', os.path.basename(root))
        for file in files:
            print(len(path) * '\t', file)


def fastq_sequences():
    """
    Function used to find all fastq files in a directory and report each file name and the percent of sequences in
    that file that are greater than 30 nucleotides long
    :return: File name and percentage
    """
    long_sequences = []
    for cur_record in SeqIO.parse(open("Sample_R1.fastq", "r"), "fastq"):
        if len(cur_record.seq) > 30:
            long_sequences.append(cur_record)
    print("Found %i sequences greater then 30 nucleotides long:" % len(long_sequences))

    for cur_record in long_sequences:
        gene_name = cur_record.name
        percentage = len(long_sequences) / len(cur_record)
        print('%s\t\t%f' % (gene_name, percentage))

print(directory_files())
print(fastq_sequences())
