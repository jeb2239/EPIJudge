from math import sqrt
from typing import List

from test_framework import generic_test

import sortedcontainers as sc


def generate_first_k_a_b_sqrt2(k) -> List[float]:
    # TODO - you fill in here.
    btree = sc.SortedSet()
    # f = a + b * 1.414
    def f(a, b): return a+b*sqrt(2)

    btree.add((0, (0, 0)))
    result = []
    for idx in range(k):
        value, startPair = btree.pop(0)

        currA, currB = startPair
        btree.add((f(currA+1, currB), (currA+1, currB)))
        btree.add((f(currA, currB+1), (currA, currB+1)))
        result.append(value)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
