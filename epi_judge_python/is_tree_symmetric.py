from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# what is the issue here
def is_symmetric(tree: BinaryTreeNode) -> bool:

    def is_sym(left,right):
        if left is None and right is None:
            return True
        if left is None:
            return False
        if right is None:
            return False
        

        if left.data != right.data:
            return False
        
        else:
            # needs to be mirrored
            return is_sym(left.left,right.right) and is_sym(left.right,right.left)

        
        
    if tree is None:
        return True
    
    return is_sym(tree.left,tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
