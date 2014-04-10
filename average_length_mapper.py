#!/usr/bin/python
import sys
import csv


def mapper():
    """
    Premise:

    If there is an answer means there is a question done before,
    so we can count the body's length for every record until the string
    nodetype "answer" changes to "question" for every node_id

    This means that the last key in every same ID group is the node
    of the question because the input's Reducer will be sorted
    by the ID and the nodetype:
    ('answer' < 'question' --> answer entries will be above of
    the question entry, after the sort and shuffle phase)

    If there is only one record PostID node, that will print 0 as mean
    because there is no answer for it

    Output:
    node_id\ttypenode\tlength's body post

    """
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_NONE)
    #Avoiding first line with titles
    reader.next()
    for line in reader:
        node_id, typenode, body, parent_id = line[0], line[5], line[4], line[6]

        if typenode == 'question':
            line = [node_id+" "+typenode]+[len(body)]
        elif typenode == 'answer':
            line = [parent_id+" "+typenode]+[len(body)]
        else:
            continue
        writer.writerow(line)

if __name__ == "__main__":
    mapper()
