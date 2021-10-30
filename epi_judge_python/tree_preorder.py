import sys
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    """
    planning:
    """
    stk=[]
    result=[(tree,'L')]
    while stk:
        (node,op)=stk.pop()

        if node is None:
            continue

        if op=='L':
            


    return result


"""

"""
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
