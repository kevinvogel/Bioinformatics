#!/usr/bin/env python
"""TICdb parser to be used for blast annotation processing to locate breakpoints."""

import csv

__author__ = "Kevin Vogel"
__email__ = "kevinvogel@mac.com"


def ticdb_parser():
    """
    This function will output the fusion sequences and gene partners in a list.
    :return: str: fusion sequence (25 bases or longer), 5' partner gene, 3' partner gene
    """
    file_name = open("TICdb_v3.3.curated.txt", "r")
    reader = csv.reader(file_name, delimiter='\t')
    for row in reader:
        order = [3, 0, 1]
        order_list = [row[i] for i in order]
        if (len(order_list[0])) >= 25:
            print order_list


if __name__ == "__main__":
    ticdb_parser()