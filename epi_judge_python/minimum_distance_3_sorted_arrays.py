from typing import List

from test_framework import generic_test
import bisect
import heapq
import sortedcontainers as sc
# look this over
def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]
                                           ) -> int:
    # TODO - you fill in here.
    # nlists pick one elem from each list
    # itrators=map(iter,sorted_arrays)
    bbt=sc.SortedSet()
    idx_arr=[0]*len(sorted_arrays)
    for i,v in enumerate(sorted_arrays):
        if len(v)>0:
            bbt.add((v[0],i))
    minDiff=float("inf")
    # [1, 2, 3] [4, 5 ,6] [ 7, 8, 9]
    # bbt = [4, 7]
    while len(bbt) == len(sorted_arrays):
        minE,listIdMin=min(bbt)
        maxE,listIdMax=max(bbt)

        if maxE-minE < minDiff:
            minDiff=maxE-minE
        # pop time
        bbt.pop(0)

        idx_arr[listIdMin]+=1
        if idx_arr[listIdMin]!=len(sorted_arrays[listIdMin]):
            bbt.add((sorted_arrays[listIdMin][idx_arr[listIdMin]],listIdMin))
        
    return minDiff
        

        

    

        
        
        
        
    
    
    
    
    return minDist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
