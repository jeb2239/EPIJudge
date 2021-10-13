from binary_tree_node import BinaryTreeNode
from test_framework import generic_test



def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    # def height(tree: BinaryTreeNode):
    #     if tree is None:
    #         return 0
        
    #     return max(height(tree.left),height(tree.right))+1


    def is_balanced(tree: BinaryTreeNode):
        
        # a tree is balanced if its left subtree and right subtree are balanced
        if tree is None:
            return (True,0)

        (leftBalance,leftHeight)=is_balanced(tree.left)
        # should do early termination here because if leftBalance is false then we can quit without
        # looking at the right side 
        (rightBalance,rightHeight)=is_balanced(tree.right)
        retval=True

        if (abs(leftHeight-rightHeight) > 1):
            retval=False
        if leftBalance is False:
            retval=False
        if rightBalance is False:
            retval=False
        
        myheight=max(leftHeight,rightHeight)+1
        return (retval,myheight)


    return is_balanced(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
