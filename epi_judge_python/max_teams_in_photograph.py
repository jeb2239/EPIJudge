import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
# wtf is going on here

class GraphVertex:
    def __init__(self) -> None:
        self.edges: List[GraphVertex] = []
        # Set max_distance = 0 to indicate unvisitied vertex.
        self.max_distance = 0


def find_largest_number_teams(graph: List[GraphVertex]) -> int:
    # TODO - you fill in here.
    def topSort(g):
        path=[]
        def dfs(currNode):
            path.append(currNode)
            for vert in currNode.edges:
                if vert.max_distance==0:
                    vert.max_distance=1
                    
                    dfs(vert)
        for node in g:
            if node.max_distance==0:
                dfs(node)
        return path

    path=topSort(graph)
    

    for i,v in enumerate(path):
        

    return 


@enable_executor_hook
def find_largest_number_teams_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(find_largest_number_teams, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_teams_in_photograph.py',
                                       'max_teams_in_photograph.tsv',
                                       find_largest_number_teams_wrapper))
