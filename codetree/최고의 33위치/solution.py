n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

start_idx = []
for i in range(n-2):
    for j in range(n-2):
        start_idx.append((i, j))

max_cnt = 0
for i, j in start_idx:
    cnt = 0
    for row in range(i, i+3):
        cnt += sum(grid[row][j:j+3])
    max_cnt = max(max_cnt, cnt)

print(max_cnt)