from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    dummyNode=ListNode(-1)
    dummyNode.next=L
    fastNode = dummyNode
    for _ in range(k):
        fastNode = fastNode.next
        
    # fast is k jumps ahead of slow
    slowNode=dummyNode
    while fastNode.next:
        slowNode = slowNode.next
        fastNode = fastNode.next

    slowNode.next=slowNode.next.next
    
    
    return dummyNode.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
