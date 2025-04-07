import sys
from collections import deque
# input = sys.stdin.readline
# import sys
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_1926\\input.txt', 'r')
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
ch = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    r = 1
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and ch[ny][nx] == False:
                    ch[ny][nx] = True
                    r += 1
                    q.append((ny, nx))

    return r

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and ch[j][i] == False:
            ch[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)
