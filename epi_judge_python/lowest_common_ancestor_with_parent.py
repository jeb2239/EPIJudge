import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # Find distance
    # of each node from the root
    """
    this did not go well lazy mind about it
    be less lazy about checking...
    """
    
    def findDepth(node):
        if node is None:
            return 0
        cnt = 0
        while node:
            node = node.parent
            cnt+=1
        return cnt

    cnt0 = findDepth(node0)
    cnt1 = findDepth(node1)
    diff = abs(cnt0-cnt1)
    if cnt0 < cnt1:
        node0, node1 = node1, node0  # node 0 is the furthest

    while diff:
        node0 = node0.parent
        diff -= 1

    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    
    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
