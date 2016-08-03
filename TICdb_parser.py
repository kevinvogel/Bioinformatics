#!/usr/bin/env python
"""TICdb parser to be used for blast annotation processing to locate breakpoints."""

import csv

__author__ = "Kevin Vogel"
__email__ = "kevinvogel@mac.com"


def ticdb_parser(file_name, min_seq_length=25):
    """
    This function will output the fusion sequences and gene partners in a list.
    :param min_seq_length: int: sequence length will be need to be a min 25 bases to be considered for blast.
    :param file_name: str: TICdb tab delimited text file "TICdb_v3.3.curated.txt".
    :return: str: fusion sequence (25 bases or longer), 5' partner gene, 3' partner gene
    """

    with open(file_name, "r") as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            order = [3, 0, 1]
            order_list = [row[i] for i in order]
            if (len(order_list[0])) >= min_seq_length:
                print order_list
        return file_name


if __name__ == '__main__':
    ticdb_parser("TICdb_v3.3.curated.txt")
