import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height, binary_tree_size, binary_tree_to_string,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# why does it need to change? why does this not work?
def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    # TODO - you fill in here.
    
    def buildMinHeight(start,end):
        if end<start:
            return None
        mid= (start+end)//2 
        
        lnode=buildMinHeight(start,mid-1)
        rnode=buildMinHeight(mid+1,end)
        newNode = BstNode(A[mid],lnode,rnode);
        return newNode
    
    v=buildMinHeight(0,len(A)-1)
    return v

@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
