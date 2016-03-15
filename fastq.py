# Recursively find all FASTQ files in a directory and report each file name and the percent of sequences in
# that file that are greater than 30 nucleotides long.

from Bio import SeqIO

__author__ = "Kevin Vogel"
__email__ = "kevinvogel@mac.com"


def fastq_sequences():
    """
    Function used to find all fastq files in a directory and report each file name and the percent of sequences in
    that file that are greater than 30 nucleotides long
    :return: File name (>30 nucleotides) and GC percentage
    """
    long_sequences = []
    for cur_record in SeqIO.parse(open("Sample_R1.fastq", "r"), "fastq"):
        if len(cur_record.seq) > 30:
            long_sequences.append(cur_record)
    print("Found %i sequences greater then 30 nucleotides long:" % len(long_sequences))

    for cur_record in long_sequences:
        gene_name = cur_record.name
        c_count = cur_record.seq.count('C')
        g_count = cur_record.seq.count('G')
        seq_length = len(cur_record.seq)
        cg_percentage = float(c_count + g_count) / seq_length
        print('%s\t\t%f' % (gene_name, cg_percentage))

print(fastq_sequences())
