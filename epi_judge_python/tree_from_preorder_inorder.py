from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    """
    need to review this problem, checkout indexing 
    """

    table = {v: k for k, v in enumerate(inorder)}  # do preprocessing here

    def binary_tree_rec(preorder_start_idx, preorder_end_idx, inorder_start_idx, inorder_end_idx):
        if preorder_start_idx >= preorder_end_idx or inorder_start_idx >= inorder_end_idx:
            return None

        rootVal = preorder[preorder_start_idx]
        sizeOfLeftSubTree = abs(table[rootVal]-inorder_start_idx)
        btn = BinaryTreeNode(rootVal)
        btn.left = binary_tree_rec(preorder_start_idx+1, preorder_start_idx +
                                   sizeOfLeftSubTree+1, inorder_start_idx, table[rootVal])
        btn.right = binary_tree_rec(
            preorder_start_idx+sizeOfLeftSubTree+1, preorder_end_idx, table[rootVal]+1, inorder_end_idx)

        return btn

    return binary_tree_rec(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
