from collections import defaultdict, deque
from typing import Set
import string
from test_framework import generic_test


def transform_string(D: Set[str], s: str, t: str) -> int:
    # TODO - you fill in here.



    q=deque([(s,0)])
    while q:
        val,dis = q.popleft()
        if val==t:
            return dis
        for i in range(len(val)):
            for c in string.ascii_lowercase:
                cand= val[:i]+c+val[i+1:]
                if  cand in D:
                    D.remove(cand)
                    q.append((cand,dis+1))
        



    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
