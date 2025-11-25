from collections import deque

n, m, r, c = map(int, input().split())
grid = [[0] * n for _ in range(n)]

queue = deque()
queue.append((r-1,c-1,0))
grid[r-1][c-1] = 1

direction = [(-1,0),(1,0),(0,1),(0,-1)]
while queue:
    x, y, t = queue.popleft()

    if t == m:
        break

    for dx, dy in direction:
        w = 2**t
        nx, ny = x + w*dx, y + w*dy
        if 0<=nx<n and 0<=ny<n and grid[nx][ny] == 0:
            queue.append((nx,ny,t+1))
            grid[nx][ny] = 1

    queue.append((x,y,t+1))

cnt = 0
for row in grid:
    cnt += sum(row)
print(cnt)