#!/usr/bin/python

import sys

sumAnswers = numberAnswers = 0

"""
Loop around the data.
Format:

(K,V) = (ID typenode, length_body)

Data comes from the mapper organized by postID and by the answer|question string
So the answers of the postID come before than the question for that postID:

ID1 "answer" Value
ID1 "answer" Value
ID1 "question" Value
ID2 "answer" Value
ID2 "question" Value
...

Output:
postID\tpostID question's len(body)\taverage len(body) of the answers

"""

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    thisKey, typeNode = data_mapped[0].strip().split()
    lengthBody = data_mapped[1]

    if typeNode == 'answer':
        numberAnswers += 1
        sumAnswers += float(lengthBody)
    else:
        print "{0}\t{1}\t{2}".format(thisKey,
                                     lengthBody,
                                     sumAnswers / numberAnswers if numberAnswers > 0 else 0)
        sumAnswers = numberAnswers = 0
