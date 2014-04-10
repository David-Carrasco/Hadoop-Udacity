#!/usr/bin/python

import sys

""" Initial Declarations """
list_hours = []
maxHour = currentNumberHours = 0
oldKey = oldHour = thisHour = None


def print_list_hours(key, hours):
    """
    Print the hours list parameter

    Arguments:
    key --> user_id
    hours --> list of the most common hours
    """
    for hour in hours:
        print key + "\t" + str(hour)


def update_list_hours(lastHour, currentHours, maximumHour, hours):
    """
    Update hours list if there is one new most repeated hour
    and update the maximumHour

    Output:
    updateHour --> counter with the number of the most common hours
    hours --> updated list with the most common hours
    """
    updateHour = maximumHour

    if currentHours > maximumHour:
            hours = [lastHour]
            updateHour = currentHours
    elif currentHours == maximumHour:
            hours.append(lastHour)

    return updateHour, hours

"""
MAIN

(K,V) = (author_id, hour)

The code calculates the most repeated hours for every author_id

Important Variables:

currentNumberHours --> Counter to trace the current repetitions of one hour in one author_id
maxHour --> the greatest number of hours repetitions of one author_id
list_hours --> List with the most repeated hours of one author_id
"""

for line in sys.stdin:
    data_mapped = line.strip().split()
    thisKey, thisHour = data_mapped[0], data_mapped[1]

    if oldKey and oldKey != thisKey:
        """ Change of author_id """

        """ Check if the last hour of the previous author_id was the most common """
        maxHour, list_hours = update_list_hours(oldHour, currentNumberHours, maxHour, list_hours)

        print_list_hours(oldKey, list_hours)
        """ Set up the variables by default in order to read the next author_id """
        maxHour, currentNumberHours, list_hours = 0, 1, []

    else:
        """ Inside a author_id """
        if oldHour and oldHour != thisHour:
            maxHour, list_hours = update_list_hours(oldHour, currentNumberHours, maxHour, list_hours)
            currentNumberHours = 1
        else:
            currentNumberHours += 1

    """ Update variables """
    oldKey, oldHour = thisKey, thisHour

""" Processing the last line of the input"""
if oldKey is not None:

    maxHour, list_hours = update_list_hours(oldHour, currentNumberHours, maxHour, list_hours)
    print_list_hours(oldKey, list_hours)
