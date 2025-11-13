'''
- 문제:
    - r,c에 적힌 값만큼 상하좌우의 칸의 값이 0으로 바뀐다.
    - 터진 칸은 사라지고 위에 있는 칸들의 값이 아래서 부터 다시 차곡차곡 쌓인다.
- 아이디어:
    - 터지는 칸들을 리스트에서 삭제하고, 나중에 리스트의 길이를 N을 만족하게끔 0을 추가

'''

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1

direction = [(-1,0),(1,0),(0,-1),(0,1)]

visited = set()
visited.add((r,c))

max_cnt = grid[r][c]-1
grid[r][c] = 0

for dx, dy in direction:
    x, y = r, c
    for _ in range(max_cnt):
        nx, ny = x+dx, y+dy

        if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
            visited.add((nx,ny))
            grid[nx][ny] = 0
            x, y = nx, ny

for j in range(n):
    col = [grid[i][j] for i in range(n) if grid[i][j] != 0]

    for i in range(n):
        grid[i][j] = 0
    
    for idx, val in enumerate(col[::-1]):
        grid[n-1-idx][j] = val

for row in grid:
    print(*row)
