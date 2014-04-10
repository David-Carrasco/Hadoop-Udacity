#!/usr/bin/python
import sys
import csv

"""
Words to check in the words list
e.g: In this case, 'Hi' and 'cheers'
"""
words = ['Hi', 'cheers']


def mapper():
    """
    Print every word of the input list words if the word is found in the body of a node
    """
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)
    #Avoiding first line with titles
    reader.next()
    for line in reader:
        """
        Convert every word of the body to compare and support case-insensitive index
        """
        body, node_id = line[4], line[0].lower()
        for word in words:
            if word.lower() in body:
                writer.writerow([word] + [node_id])

if __name__ == "__main__":
    mapper()
