n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

if m == 1:
    print(2 * n)
    exit()

cnt = 0

# 각 행마다 검사
for i in range(n):
    flag = 1
    for j in range(n-1):
        if grid[i][j] == grid[i][j+1]:
            flag += 1
        if grid[i][j] != grid[i][j+1]:
            flag = 1
        if flag >= m:
            cnt += 1
            break

for j in range(n):
    flag = 1
    for i in range(n-1):
        if grid[i][j] == grid[i+1][j]:
            flag += 1
        if grid[i][j] != grid[i+1][j]:
            flag = 1
        if flag >= m:
            cnt += 1
            break

print(cnt)