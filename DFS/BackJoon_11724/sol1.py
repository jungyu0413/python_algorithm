import sys
from collections import deque
# input = sys.stdin.readline
# import sys
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_11724\\input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

def dfs(x):
    visited[x] = True
    for j in board[x]:
        if not visited[j]:
            dfs(j)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)