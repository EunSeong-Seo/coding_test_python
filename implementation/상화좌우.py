n = int(input())
plans = input().split()

x,y = 1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
dir = ['L','R','D','U']

for plan in plans:
    for i in range(len(dir)):
        if plan == dir[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x,y)