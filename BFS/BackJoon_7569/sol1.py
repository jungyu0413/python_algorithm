
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_7569\\input.txt', 'r')
# import sys
import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split()) # 가로, 세로, 높이
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dy = [0, 1, 0, -1, 0, 0]
dx = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

for k in range(h):
    for j in range(n):
        for i in range(m):
            if board[k][j][i] == 1:
                q.append((k, j, i))

while q:
    z, y, x = q.popleft()
    for pick in range(6):
        nz = z + dz[pick]        
        ny = y + dy[pick]
        nx = x + dx[pick]
        if 0<=ny<n and 0<=nx<m and 0<=nz<h:
            if board[nz][ny][nx] == 0:
                board[nz][ny][nx] = board[z][y][x] + 1
                q.append((nz, ny, nx))
                
 
            
ans = 0
for k in range(h):
    for j in range(n):
        for i in range(m):
            if board[k][j][i] == 0:
                print(-1)
                sys.exit(0)
            ans = max(ans, board[k][j][i])
            
            
print(ans-1)