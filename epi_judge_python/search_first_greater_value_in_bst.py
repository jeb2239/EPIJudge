from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    # TODO - you fill in here.
    minval = float("inf")
    minValNode = None

    def aux(tree):
        nonlocal minval
        nonlocal minValNode
        if tree is None:
            return

        if k < tree.data:
            # might be in left
            # if minval > tree.data: this will always be the case because any number we would have seen before this would have to
            # be bigger via the BST property so this is a moot point
            minval = tree.data
            minValNode = tree
            aux(tree.left)
        else:
            aux(tree.right)

    aux(tree)
    return minValNode


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
