import collections


def XO(s):
	s = s.lower()  # SHouldn't be case-sensitive
    count = collections.Counter(s)
    if count['x'] == count['o']:
        return true
    else:
        return False

