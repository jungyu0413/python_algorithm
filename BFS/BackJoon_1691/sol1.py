import sys
from collections import deque
# input = sys.stdin.readline
# import sys
sys.stdin = open('C:\\Users\\Lee\\Desktop\\algorithm\\BFS\\BackJoon_1697\\input.txt', 'r')
# import sys
# from collections import deque
n, k = map(int, input().split())
visited = [False] * 100001
dist = [0] * 100001

def bfs(x):
    if x == k:
        return 0
    visited[x] = True
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for next in [now-1, now+1, now*2]:
            if 0<=next<=100000:
                if visited[next] == False:
                    visited[next] = True
                    dist[next] = dist[now] + 1
                    q.append(next)
                if next == k:
                    return dist[next]

print(bfs(n))