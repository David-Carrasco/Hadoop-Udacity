#!/usr/bin/python
import sys
import csv


def mapper():
    """
    Get the fields author_id and reputation to calculate the top 10
    in the Reducer
    """
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)
    #Avoiding first line with titles
    reader.next()
    for line in reader:
        author_id, reputation = line[0], line[1]
        writer.writerow([author_id]+[reputation])

if __name__ == "__main__":
    mapper()
