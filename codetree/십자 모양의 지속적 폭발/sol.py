n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input())-1 for _ in range(m)]

def find_i(command):
    for i in range(n):
        if grid[i][command] != 0:
            return i
    return -1

direction = [(-1,0), (1,0), (0,-1), (0,1)]

for command in commands:
    i = find_i(command)
    if i == -1: # 해당 열이 모두 0일 경우
        continue
    
    max_cnt = grid[i][command]
    grid[i][command] = 0
    visited = set()
    visited.add((i,command))
    for dx, dy in direction:
        x, y = i, command
        for _ in range(max_cnt-1):
            nx, ny = x + dx, y + dy
            if 0<= nx < n and 0<= ny < n and (nx,ny) not in visited:
                grid[nx][ny] = 0
                x, y = nx, ny
    
    for j in range(n):
        col = [grid[i][j] for i in range(n) if grid[i][j] != 0]

        for i in range(n):
            grid[i][j] = 0

        curr_n = n-1
        for val in col[::-1]:
            grid[curr_n][j] = val
            curr_n -= 1
    
for row in grid:
    print(*row)