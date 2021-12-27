#print the number of non cap sensitive duplicate items


def duplicate_count(text):
    from collections import Counter
    text = text.lower()
    count = 0
    a = dict(Counter(text))
    return(sum(1 for i in a.values() if i > 1))

print(duplicate_count("abc1C1"))
