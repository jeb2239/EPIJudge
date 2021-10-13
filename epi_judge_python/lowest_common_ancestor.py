import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# invalid in put, can i be ancestor of myself?
# took 3 runs


def lcaBetter(tree, node0, node1):

    def lcaRec(root):
        if root is None:
            return (0, None)  # num of nodes in subtree and lca

        totalNodes = 0
        
        if root is node0:
            totalNodes += 1
            

        if root is node1:
            totalNodes += 1
            

        amtL, lcaL = lcaRec(root.left)
        amtR, lcaR = lcaRec(root.right)
        if amtL==2:
            return (amtL,lcaL)
        if amtR==2:
            return (amtR,lcaR)

        
        totalNodes+=amtL
        totalNodes+=amtR
        return (totalNodes,root)

    return lcaRec(tree)[1]
        
        

        


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    if tree is None:
        return None

    def lcaRec(root, pathList, target):
        if root is None:
            return False

        if root is target:
            pathList.append(target)
            return True

        pathList.append(root)
        if lcaRec(root.right, pathList, target):
            return True
        if lcaRec(root.left, pathList, target):
            return True
        pathList.pop()
        return False

    p1 = []
    p2 = []
    lcaRec(tree, p1, node0)
    lcaRec(tree, p2, node1)

    i = 0
    while i < len(p1) and i < len(p2) and p1[i] == p2[i]:
        i += 1

    return p1[i-1]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lcaBetter, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
