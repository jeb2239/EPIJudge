from collections import deque
from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:

    nrows = len(board)
    ncols = len(board[0])

    q = deque()

    for row in range(nrows):
        for col in range(ncols):
            if board[row][col] == "W":
                if row == 0 or col == 0 or row == nrows-1 or col == ncols-1:
                    q.append((row, col))
                    board[row][col]="T"

    while q:
        row, col = q.popleft()

        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            newRow = d[0]+row
            newCol = d[1]+col
            inbounds = (0 <= newRow < nrows and 0 <= newCol < ncols)
            if inbounds and board[newRow][newCol] == "W":
                board[newRow][newCol] = "T"
                q.append((newRow, newCol))

    for row in range(nrows):
        for col in range(ncols):
            if board[row][col] == 'W':
                board[row][col] = 'B'

    for row in range(nrows):
        for col in range(ncols):
            if board[row][col] == 'T':
                board[row][col] = 'W'
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
