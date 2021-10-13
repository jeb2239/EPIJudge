from typing import List

from test_framework import generic_test
import bisect

# look this over
def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]
                                           ) -> int:
    # TODO - you fill in here.
    A=sorted_arrays[0]
    B=sorted_arrays[1]
    C=sorted_arrays[2]
    
    minDist=float("inf")
    i=j=k=0
    while i < len(A) and j<len(B) and k<len(C):


        minVal=min(A[i],B[j],C[k])
        maxVal=max(A[i],B[j],C[k])
        minDist=min(maxVal-minVal,minDist)  
        if A[i]==minVal:
            i+=1
        elif B[j]==minVal:
            j+=1
        else:
            k+=1


    
    
    return minDist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
