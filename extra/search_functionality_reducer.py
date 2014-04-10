#!/usr/bin/python

import sys

oldKey = None
sumAppearances = 0
list_nodes = []

# Loop around the data
# It will be in the format key\tval

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, node_id = data_mapped

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}\t{2}".format(oldKey, sumAppearances, sorted(list_nodes))
        oldKey = thisKey
        sumAppearances = 0
        list_nodes = []

    oldKey = thisKey
    sumAppearances += 1
    list_nodes.append(int(node_id))

if oldKey is not None:
    print "{0}\t{1}\t{2}".format(oldKey, sumAppearances, sorted(list_nodes))
