import sys
from collections import deque
# input = sys.stdin.readline
# import sys
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_1926\\input.txt', 'r')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 8방향: 상하좌우 + 대각선
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    m, n = map(int, input().split())  # 가로, 세로
    if m == 0 and n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    def dfs(y, x):
        visited[y][x] = True
        for k in range(8):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 1 and not visited[ny][nx]:
                    dfs(ny, nx)

    cnt = 0
    for j in range(n):
        for i in range(m):
            if board[j][i] == 1 and not visited[j][i]:
                dfs(j, i)
                cnt += 1

    print(cnt)