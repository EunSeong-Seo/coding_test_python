from collections import deque
from lib2to3.pgen2.token import GREATEREQUAL

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    queue = deque()             # queue 만들기
    queue.append((x,y))         # 초기좌표 추가하기
    while queue:                # queue가 빌 때까지 반복하기
        x, y = queue.popleft()  # 하나 꺼내고 

        for i in range(4):      # 움직이는데
            nx = x + dx[i]
            ny = y + dy[i]
                                # 무시조건들 추가 
            if nx < 0 or nx >=n or ny < 0 or ny >=m: #맵을 나간경우
                continue
            if graph[nx][ny] == 0: # 길이 아닌경우 
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1     # 이경우는 따로 visited 를 선정하지 않음
                queue.append((nx,ny))

    return graph[n -1][m - 1]

print(bfs(0,0))
