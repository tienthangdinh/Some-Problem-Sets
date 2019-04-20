from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    randomlist1 = a.split('\n')
    randomlist2 = b.split('\n')
    randomset1 = set()
    randomset2 = set()
    alist = []
    for i in randomlist1:
        randomset1.add(i)
    for i in randomlist2:
        randomset2.add(i)
    for i in randomset1:
        for j in randomset2:
            if i == j:
                alist.append(i)
    return alist


def sentences(a, b):
    """Return sentences in both a and b"""
    set1 = set()
    set2 = set()
    list1 = sent_tokenize(a, language='english')
    list2 = sent_tokenize(b, language='english')
    alist = []
    for i in list1:
        set1.add(i)
    for i in list2:
        set2.add(i)
    print(set1)
    print(set2)
    for i in set1:
        for j in set2:
            if i == j:
                alist.append(i)

    return alist


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    set1 = set()
    set2 = set()
    alist = []
    for i in range(len(a) - n + 1):
        randomstring = a[i:i + n]
        set1.add(randomstring)
    for i in range(len(b) - n + 1):
        randomstring = b[i:i + n]
        set2.add(randomstring)
    for i in set1:
        for j in set2:
            if i == j:
                alist.append(i)

    return alist
