from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:

    def rebuild_bst(seq):

        if len(seq) == 0:
            return None

        """
        so each subtree 
        """
        rootval = seq[0]
        idx = 1
        while idx < len(seq) and seq[0] > seq[idx]:
            idx += 1

        nodeL = rebuild_bst(seq[1:idx])
        nodeR = rebuild_bst(seq[idx:])

        return BstNode(rootval, nodeL, nodeR)

    return rebuild_bst(preorder_sequence)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
