
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_7562\\input.txt', 'r')
# import sys
import sys
from collections import deque
input = sys.stdin.readline
c = int(input())


dy = [-1, -1, -2, -2, 1, 1, 2, 2]
dx = [2, -2, 1, -1, 2, -2, 1, -1]

for _ in range(c):
    N = int(input())
    st_x, st_y = map(int, input().split())
    ed_x, ed_y = map(int, input().split())
    
    board = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    
    def bfs(y, x):
        q = deque()
        q.append((y, x))
        visited[y][x] = True
        while q:
            ey, ex = q.popleft()
            if ey == ed_y and ex == ed_x:
               return board[ey][ex]
            for k in range(8):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if 0<=ny<N and 0<=nx<N:
                    if visited[ny][nx] == False:
                        visited[ny][nx] = True
                        board[ny][nx] = board[ey][ex] + 1
                        q.append((ny, nx))

                        
    print(bfs(st_y, st_x))