from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.

    def is_binary_tree_bst(tree,lower_bound=float("-inf"),upper_bound=float("inf")):

        if tree is None:
            return True

        
        if not (lower_bound <= tree.data <= upper_bound):
            return False

        isBstL=is_binary_tree_bst(tree.left,lower_bound=lower_bound,upper_bound=tree.data)
        isBstR=is_binary_tree_bst(tree.right,lower_bound=tree.data,upper_bound=upper_bound)

        return isBstL and isBstR

    return is_binary_tree_bst(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
