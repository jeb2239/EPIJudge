from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# this was horrible it took you way too many tries, short attention span ahhhhhh
def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    if L is None:
        return None
    if start==finish:
        return L
    startNode=L
    endNode=L
    
    start-=1
    finish-=1
    # push the endNode ahead of the startNode by finish-start slots

    for _ in range(finish-start):
        endNode=endNode.next
    dummyNode=ListNode(-1)
    dummyNode.next=L
    
    prev=dummyNode
    for _ in range(start):
        prev=startNode
        startNode=startNode.next
        endNode=endNode.next

    headHandle=prev
    endHandle=endNode.next
    prev=endHandle
    currNode=headHandle.next
    
    while currNode is not endHandle:

        oldNext=currNode.next
        currNode.next=prev
        prev=currNode #the next node will change its pointer to point at this
        currNode=oldNext

    # at the end 
    headHandle.next=endNode
    return dummyNode.next
    



    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
