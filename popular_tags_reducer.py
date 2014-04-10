#!/usr/bin/python

import sys

"""
Format input:
(K,V) = (tag_name, )

Format output of top 10:
tag_name\tnumber of appearances tag_name
"""
tags = {}

"""
Loop around the data.
Create a dictionary to save the sum of every key found in the input
"""
for line in sys.stdin:
    tag = line.strip()
    if tag in tags:
        tags[tag] += 1
    else:
        tags[tag] = 1

"""
Sort the dictionary by the value from the greatest to the smallest number
"""
sort = sorted(tags.items(), key=lambda x: x[1], reverse=True)

"""
Print 10 tags with more appearances
"""
for _ in range(0, 10):
    print "{0}\t{1}".format(sort[_][0],sort[_][1])
