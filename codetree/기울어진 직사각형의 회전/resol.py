from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())
r, c = r-1, c-1

nums = deque([grid[r][c]])
idxs = [(r,c)]

for _ in range(m1):
    nx, ny = r-1, c+1
    nums.append(grid[nx][ny])
    idxs.append((nx,ny))
    r, c = nx, ny

for _ in range(m2):
    nx, ny = r-1, c-1
    nums.append(grid[nx][ny])
    idxs.append((nx,ny))
    r, c = nx, ny

for _ in range(m3):
    nx, ny = r+1, c-1
    nums.append(grid[nx][ny])
    idxs.append((nx,ny))
    r, c = nx, ny

for _ in range(m4-1):
    nx, ny = r+1, c+1
    nums.append(grid[nx][ny])
    idxs.append((nx,ny))
    r, c = nx, ny

if dir == 0:
    nums.rotate(1)
else:
    nums.rotate(-1)

for x, y in idxs:
    grid[x][y] = nums.popleft()

for row in grid:
    print(*row)