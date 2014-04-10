#!/usr/bin/python

import sys

oldKey = None
authorsInfluence = {}

"""
Loop around the data. It will be in the format key\tval where:
key is the id_node "Q" | abs_parent_id "X"
val is the author_id

Output:
node_id\t[(author_id1, intensity1), (author_id2, intensity2), ...]
"""

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    thisKey, author = data_mapped[0].split()[0], data_mapped[1]

    if oldKey and oldKey != thisKey:
        # Change KEY
        print "{0}\t{1}".format(oldKey, [(x, y) for x, y in authorsInfluence.items()])
        authorsInfluence = {}

    if author in authorsInfluence:
        authorsInfluence[author] += 1
    else:
        authorsInfluence[author] = 1

    oldKey = thisKey

# Processing the last line
if oldKey is not None:
    print "{0}\t{1}".format(oldKey, [(x, y) for x, y in authorsInfluence.items()])
