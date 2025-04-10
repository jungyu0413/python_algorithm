import sys
from collections import deque
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_2606\\input.txt', 'r')
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

visited = [False] * (n+1)
board = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    board[x][y] = 1
    board[y][x] = 1
    
def dfs(x):
    visited[x] = True
    cnt = 0
    for i in range(1, n+1):
        if board[x][i] == 1 and not visited[i]:
            visited[i] = True
            cnt += 1
            cnt += dfs(i)
    return cnt


print(dfs(1))
