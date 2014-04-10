#!/usr/bin/python
import sys
import csv


def mapper():
    """
    Split all tags in the tagnames field of the input file
    and print them one by one per line
    """
    reader = csv.reader(sys.stdin, delimiter='\t')
    #Avoiding first line with titles
    reader.next()
    for line in reader:
        """
        Print every tag of the tag_names string to be counted in the Reducer
        """
        tag_names = line[2].split()
        for tag in tag_names:
            print tag

if __name__ == "__main__":
    mapper()
