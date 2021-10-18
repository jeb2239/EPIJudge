from typing import List, Optional

from list_node import ListNode
from test_framework import generic_test

# you ran this once and messed up be more careful or i will beat you
# you must must must check for nulllllll either L1 or L2
# ok just being lazy at this point
# this should be correct 1st shot
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    dummyOut=ListNode(-1)
    headOfL=dummyOut
    currNode1=L1
    currNode2=L2
    while currNode1 and currNode2:
        if currNode1.data < currNode2.data:
            dummyOut.next=currNode1
            currNode1=currNode1.next
            dummyOut=dummyOut.next
        else:
            dummyOut.next=currNode2
            currNode2=currNode2.next
            dummyOut=dummyOut.next
    
    if currNode1:
        dummyOut.next=currNode1
    
    if currNode2:
        dummyOut.next=currNode2

    return headOfL.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
