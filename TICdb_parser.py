#!/usr/bin/env python
"""TICdb parser to be used for blast annotation processing to locate breakpoints."""

import os
import csv
import subprocess

__author__ = "Kevin Vogel"
__copyright__ = "Copyright 2016, ArcherDX"
__credits__ = ["Kevin Vogel"]
__version__ = "0.1"
__maintainer__ = "Kevin Vogel"
__email__ = "kvogel@archerdx.com"
__status__ = "Development"


def main():
    dir_name = "./bed_files/"
    os.mkdir(dir_name)
    for entry in ticdb_parser('TICdb_v3.3.curated.txt'):
        bed_file_name = "{}.bed".format(entry[1].replace(',', '_'))
        bed_file_name = os.path.join(dir_name, bed_file_name)
        subprocess.check_output(
            ['blastit.py', "--seq", entry[0], "--target_genes", entry[1], "--out_bed", bed_file_name, "--max_hits",
             "2"])


def ticdb_parser(file_name, min_seq_length=25):
    """
    This function will output the fusion sequences and gene partners in a list.
    :param min_seq_length: int: sequence length will be need to be a min 25 bases to be considered for blast.
    :param file_name: str: TICdb tab delimited text file 'TICdb_v3.3.curated.txt'.
    :return: str: fusion sequence (25 bases or longer), 5' partner gene, 3' partner gene
    """

    with open(file_name, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            order = [3, 0, 1]
            order_list = [row[i] for i in order]
            if (len(order_list[0])) >= min_seq_length:
                gene_fusion_name = "{},{}".format(order_list[1], order_list[2])
                yield [order_list[0], gene_fusion_name]


if __name__ == '__main__':
    main()
