import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:
    """
    have two nodes a slow node and a fast node
    fastNode moves twice as fast 
    if the list has an end the fast node should reach it before the slow node
    if it doesn't have an end then the fast node should lap the slow node inside the cycle

    once i have figured out the overlap - i need to find first node of cycle
    need to find size of cycle hold one node steady and count around until you see that node again
    this will give you the size of the cycle

    cycle_sz=N
    you will then need
    
    
    """
    if head is None:
        return None
    dummyNode=ListNode(-1)
    dummyNode.next=head
    currNode=dummyNode.next
    # one mistake here was starting the fast pointer at the same spot as currNode, should be started one slot over
    fastNode=dummyNode.next.next # i was missing the additional next 
    while fastNode and fastNode.next and fastNode is not currNode:
        currNode=currNode.next
        fastNode=fastNode.next.next
        
    if fastNode is not currNode:
        return None
    # otherwise we know for a fact there is a loop
    # now must find the start + size of that loop
    # startCycle + k = idxWeStopAt
    # if i know the size of the cycle what if I keep a node exactly cycle size slots ahead of my current node
    # 

    currNode=fastNode.next
    count=0 # amount of nodes
    print("he")
    while currNode and currNode is not fastNode:
        count+=1
        currNode=currNode.next
    count+=1
    if currNode is None:
        return None
    
    fastNode=dummyNode.next
    # fastNode is idx into m + k = cycle_size, 
    while count:
        fastNode=fastNode.next
        count-=1
    
    currNode=dummyNode.next
    while currNode is not fastNode:
        currNode=currNode.next
        fastNode=fastNode.next

    
    return currNode


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
