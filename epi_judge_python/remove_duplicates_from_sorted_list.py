from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    if L is None:
        return None
    dummyOne = ListNode(-1)
    dummyOne.next = L
    if dummyOne.next.next is None:
        return dummyOne.next
    currNode = dummyOne.next.next
    prevNode = dummyOne.next
    while currNode:
        if prevNode.data == currNode.data:
            # delete currNode
            prevNode.next = currNode.next
            currNode = currNode.next
        else:
            prevNode = prevNode.next
            currNode = currNode.next

    return dummyOne.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
