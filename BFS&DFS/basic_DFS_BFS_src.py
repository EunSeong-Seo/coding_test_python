def dfs(graph, v, visited):
    # 1.현재 노드를 방문처리
    visited[v] = True
    print(v,end=' ')
    # 2. 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


from collections import deque

def bfs(graph,start,visited):
    # 1. queue 구현
    queue = deque([start])
    # 2. 현재노드를 방문처리 
    visited[start] = True
    # 3. 큐가 빌때까지 반복
    while queue:
        # 4. 큐에서 하나의 원소르 뽑아출력하기 
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
 
    