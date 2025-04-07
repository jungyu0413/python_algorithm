import sys
from collections import deque
# input = sys.stdin.readline
# import sys
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_1926\\input.txt', 'r')

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
ch = [[False] * N for _ in range(N)]
each = 0
result = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if map[ny][nx] == 1 and ch[ny][nx] == False:
                ch[ny][nx] = True
                dfs(ny, nx)   




for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and ch[j][i] == False:
            ch[j][i] = True
            each = 0
            dfs(j, i)
            result.append(each)


print(len(result))

for i in result:
    print(i)