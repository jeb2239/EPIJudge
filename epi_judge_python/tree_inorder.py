from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# use new technique
# try leetcode binary tree iterator


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stk = [(tree, 'L')]
    result = []
    while stk:
        node, op = stk.pop()
        if node is None:
            continue
        elif op == 'L':
            stk.append((node, 'D'))
            stk.append((node.left, 'L'))
        elif op == 'D':
            result.append(node.data)
            stk.append((node.right, 'L'))
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
