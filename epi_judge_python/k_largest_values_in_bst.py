from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # TODO - you fill in here.

    # just do a backwards inorder traversal
    nodeOfInterest = None
    k = k
    result = []

    def decreasingBST(tree):
        if tree is None:
            return
        
        nonlocal k
        if k == 0:
            return

        decreasingBST(tree.right)
        k -= 1  # at max val we do largest, then second largest
        if k >= 0:
            result.append(tree.data)
        else:
            return

        decreasingBST(tree.left)

    decreasingBST(tree)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
