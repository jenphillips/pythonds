def findAnagram0(s1, s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


def findAnagram1(str1, str2):
    ''' Determine whether 2 strings are anagrams by checking off matching
    characters.
    '''
    isAnagram = False

    list1 = list(str1)

    for ch in str2:
        if ch in str1:
            # Character matches; check it off
            i = list1.index(ch)
            list1.pop(i)

    print list1
    if len(list1) is 0:
        # All characters matched and were checked off
        isAnagram = True

    return isAnagram
