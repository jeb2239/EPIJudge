import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def listLen(l:ListNode):
    currNode=l
    count=0
    while currNode:
        count+=1
        currNode=currNode.next
    
    return count
    

def overlapping_lists(l0: ListNode, l1: ListNode) -> ListNode:
    # first see which list is longer
    if l0 is None:
        return None
    if l1 is None:
        return None
    biggerList=None
    smallerList=None
    len1=listLen(l0)
    len2=listLen(l1)
    # always screw up booleans like having greater than sign backwards it is bad
    if len1 > len2:
        biggerList=l0
        smallerList=l1
    else:
        biggerList=l1
        smallerList=l0
    diff=abs(len1-len2)

    while biggerList and diff:
        biggerList=biggerList.next
        diff-=1
    
    while biggerList and smallerList and (biggerList is not smallerList):
        biggerList=biggerList.next
        smallerList=smallerList.next
    
    # if biggerList is None or smallerList is None:
    #     return None
    # print(biggerList.data)

    return biggerList


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    # TODO - you fill in here.
    return overlapping_lists(l0,l1)


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
