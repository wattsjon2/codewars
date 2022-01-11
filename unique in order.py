#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

from typing import Sequence


def unique_in_order(iterable):
    sequenceList = []
    for x in iterable:
        if sequenceList == []:
            sequenceList.append(x)
        else:
            if sequenceList[-1] != x:
                sequenceList.append(x)
    return sequenceList


print(unique_in_order('AAAABBBCCDAABBB'))