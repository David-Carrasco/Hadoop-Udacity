#!/usr/bin/python
import sys
import csv


def mapper():
    """
    Output:
    user_id(column3)\tadded_at(column8 hour --> positions 11 to 13)

    The reducer will sort by author_id " " hour, namely:

    1000003 00
    1000003 04
    1000004 02
    1000004 08
    1000004 12
    1000005 00
    ...

    """
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)
    #Avoiding first line with titles
    reader.next()
    for line in reader:
        author_id, added_at_hour = line[3], line[8][11:13]
        writer.writerow([author_id + " " + added_at_hour])

if __name__ == "__main__":
    mapper()
