import sys
from collections import deque
# input = sys.stdin.readline
# import sys
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_2178\\input.txt', 'r')

import sys
from collections import deque
# input = sys.stdin.readline()
n, m = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(n)]
ch = [[False] * m for _ in range(n)]
# for문 1에서만 출발 1이 있는 경우 방문
# 4,6에서 stop

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
q = deque()

def bfs(y, x):
    rs = 1
    q.append((y, x))
    ch[y][x] = True
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and ch[ny][nx] == False:
                    ch[ny][nx] = True
                    rs += 1
                    map[ny][nx] = map[ey][ex] + 1
                    q.append((ny, nx))
                    if ny == n-1 and nx == m-1:
                        return map[ny][nx]
    

print(bfs(0, 0))