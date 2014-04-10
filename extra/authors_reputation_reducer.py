#!/usr/bin/python

import sys

"""
Format input:
(K,V) = (author_id, reputation)

Format output of top 10:
author_id
"""
authors = {}

"""
Loop around the data.
Create a dictionary with every author of the input
"""
for line in sys.stdin:
    author_id, reputation = line.strip().split()
    authors[author_id] = int(reputation)

"""
Sort the dictionary by the reputation from the greatest to the smallest number
"""
sort = sorted(authors.items(), key=lambda x: x[1], reverse=True)

"""
Print 10 authors with more reputation
"""
for _ in range(0, 10):
    print "{0}\t{1}".format(sort[_][0],sort[_][1])
