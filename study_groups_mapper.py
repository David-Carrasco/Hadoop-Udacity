#!/usr/bin/python
import sys
import csv


def mapper():
    """
    Structure sorted as reducer's input:
    id_node_question "Q"(if typenode == question)
    id_node_question(abs_parent_id) "X"(typenode == answer or comment) author_id

	Example after hadoop sorts the mapper's output by the id_node_question and type ("Q" or "X")
	so that the question node is always in the top of each group since "Q" < "X" in the sort:

    1000001 Q
    1000001 X 1123
    1000001 X 34324
    ...
    1000004 Q
    1000004 X 4234
    ...

	The "Q" in the type will mean the node is a node question and every answer or comment node
	will have the type "X". The abs_parent_id of these last nodes matches with the question node_id
    """

    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_NONE)
    #Avoiding first line with titles
    reader.next()
    for line in reader:
        node_id, typenode, abs_parent_id, author_id = line[0], line[5], line[7], line[3]
        if typenode == 'question':
            line = [node_id + " " + "Q"]+[author_id]
        else:
            line = [abs_parent_id + " " + "X"]+[author_id]
        writer.writerow(line)

if __name__ == "__main__":
    mapper()
