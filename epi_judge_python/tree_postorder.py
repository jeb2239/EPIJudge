from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# LRD
def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result=[]
    stk=[(tree,'L')]
    while stk:

        (node,op)=stk.pop()
        if node is None:
            continue
        
        if op=='L':
            stk.append((node.left,'L'))
            stk.append((node.right,'L'))
            stk.append((node,'D'))
            
        if op=='D':
            result.append(node.data)

            


    result.reverse()
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
