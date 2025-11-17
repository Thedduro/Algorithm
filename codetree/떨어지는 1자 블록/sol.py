n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
for i in range(n):
    row = grid[i]
    if 1 in row[k-1:k-1+m]:
        break
    else:
        can = i

for j in range(k-1, k-1+m):
    grid[can][j] = 1

for row in grid:
    print(*row)