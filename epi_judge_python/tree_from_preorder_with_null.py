import functools
from typing import Deque, List
from collections import deque
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    # you need to look for two nulls, anything that comes after two nulls is a leaf 
    def reconstruct_helper(q):
        curr_key=q.popleft()
        if curr_key is None:
            return None

        
        left_node=reconstruct_helper(q)
        right_node=reconstruct_helper(q)
        return BinaryTreeNode(curr_key,left_node,right_node)
    return reconstruct_helper(deque(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))


class Solution:
    def solve(self, board):
        n = len(board)
        m = len(board[0])

        def get_val(dp, a, b):
            if a >= 0 and a < n and b >= 0 and b < m:
                return dp[a][b]
            return -float('inf')

        tl = [[-float('inf')] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                tl[i][j] = max(get_val(tl, i-1, j), get_val(tl, i, j-1), board[i][j])

        tr = [[-float('inf')] * m for i in range(n)]
        for i in range(n):
            for j in range(m-1, -1, -1):
                tr[i][j] = max(get_val(tr, i-1, j), get_val(tr, i, j+1), board[i][j])
        
        bl = [[-float('inf')] * m for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m):
                bl[i][j] = max(get_val(bl, i+1, j), get_val(bl, i, j-1), board[i][j])
        
        br = [[-float('inf')] * m for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                br[i][j] = max(get_val(br, i+1, j), get_val(br, i, j+1), board[i][j])

        dp = [[-float('inf')] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                vals = []
                vals.append(get_val(tl, i-1, j-1))
                vals.append(get_val(tr, i-1, j+1))
                vals.append(get_val(bl, i+1, j-1))
                vals.append(get_val(br, i+1, j+1))
                dp[i][j] = max(vals)

        ans = -float('inf')
        for i in range(n):
            for j in range(m):
                ans = max(ans, board[i][j] + dp[i][j])
        return ans
