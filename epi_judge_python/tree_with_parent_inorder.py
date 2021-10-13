from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

# morris traversal


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    currNode=tree
    prev,result=None,[]

    # if currNode is none that means we just popped up from the root node which has a parent of None
    while currNode:
        
        

        if prev is currNode.left:
            # we just finished our left sub tree
            # need to visit this
            
            result.append(currNode.data)
            if currNode.right:
                prev=currNode
                currNode=currNode.right
            else:
                # if there is no right side to visit then 
                # just go up one node
                prev=currNode
                currNode=currNode.parent
            
            continue
            

        if prev is currNode.parent or prev is None:
            # we are going down into the tree
            prev=currNode
            currNode=currNode.left
            continue

        if prev is currNode.right:
            # we must have already visited this node 
            # according the in order traversal spec
            prev = currNode
            currNode=currNode.parent
            continue
    

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
