import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    currNode = tree.left
    leftSide = []
    leftSide.append(tree)

    while currNode:
        leftSide.append(currNode)
        if currNode.left:
            currNode = currNode.left
        else:
            currNode = currNode.right

    currNode = tree.right
    rightSide = []
    while currNode:
        rightSide.append(currNode)
        if currNode.right:
            currNode = currNode.right
        else:
            currNode = currNode.left

    leaves = []

    def trav(root):
        if root is None:
            return
        if root.left is None and root.right is None:
            leaves.append(root)
            return

        trav(root.left)
        trav(root.right)
        return

    trav(tree)

    rightSide.reverse()
    # rightSide.pop()
    if len(leaves)==1:
        return leftSide+leaves+rightSide
    return leftSide+leaves[1:len(leaves)-1]+rightSide


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
