import sys
from collections import deque
# input = sys.stdin.readline
# import sys
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_7576\\input.txt', 'r')
# import sys

input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

q = deque()

for j in range(n):
    for i in range(m):
        if board[j][i] == 1:
            q.append((j, i))  # ✅ 좌표 넣기

# 토마토 번식 bfs
while q:
    y, x = q.popleft()
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                q.append((ny, nx))

# 출력
ans = 0
for j in range(n):
    for i in range(m):
        if board[j][i] == 0:
            print(-1)
            sys.exit(0)
        ans = max(ans, board[j][i])  # ✅ anx → ans 수정

print(ans - 1)