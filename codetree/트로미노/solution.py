n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

blocks = [
    [(0,0),(1,0),(1,1)],   # └ 모양
    [(0,0),(0,1),(1,0)],   # ┌ 모양
    [(0,0),(0,1),(1,1)],  # ┐ 모양
    [(0,0),(1,0),(1,-1)],  # ┘ 모양
    [(0,0),(0,1),(0,2)],   # ㅡ 모양
    [(0,0),(1,0),(2,0)]   # | 모양
]

max_sum = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            cnt = 0
            valid = True
            for dx, dy in block:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0<= ny < m:
                    cnt += grid[nx][ny]
                else:
                    valid = False
                    break
            if valid:
                max_sum = max(max_sum, cnt)

print(max_sum)