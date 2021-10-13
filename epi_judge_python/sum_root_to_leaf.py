from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# this is not going well
# could use addtition space here


def sum_root_to_leaf_try1(tree: BinaryTreeNode):
    total = 0

    def sum_r_to_l(root, currSum):
        nonlocal total

        if root is None:
            return

        if root.left is None and root.right is None:
            # is leaf
            currSum = currSum*2+root.data
            total += currSum

        currSum = currSum*2 + root.data

        sum_r_to_l(root.left, currSum)
        sum_r_to_l(root.right, currSum)

        return
    sum_r_to_l(tree, 0)
    return total


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    return sum_root_to_leaf_try1(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
