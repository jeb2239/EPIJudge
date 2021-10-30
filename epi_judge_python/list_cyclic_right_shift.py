from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# need help with this one come back and review it please


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    # why are linklists so baaaaaaaddd
    if not L:
        return L
    n = 1
    currNode = L
    while currNode.next:
        n += 1
        currNode = currNode.next

    k %= n

    oldLastNode = currNode
    # need to make a circle with this oldLastNode and head
    assert oldLastNode.next is None
    oldLastNode.next = L
    # where do we clip the new tail node
    # we do this at n-k
    currNode = L

    # need to checkout off by one stuff
    
    for _ in range(n-k-1):
        # 1 2 3  -> 3 1 2
        # 1,2,3,4,5,6 => k =1=> 6 1 2 3 4 5
        currNode = currNode.next

    newHead = currNode.next
    currNode.next = None
    return newHead


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
