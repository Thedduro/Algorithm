n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = r-1, c-1

from collections import deque
queue = deque([])
queue.append((r,c))

result = [grid[r][c]]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

while queue:
    x, y = queue.popleft()

    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and grid[x][y] < grid[nx][ny]:
            queue.append((nx,ny))
            result.append(grid[nx][ny])
            break

print(*result)