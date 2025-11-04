n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def check(i, j):
    mcnt = 0
    for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0<= nj < n:
            if grid[ni][nj] == 1:
                mcnt += 1
    if mcnt >= 3:
        return True
    else:
        return False

cnt = 0
for i in range(n):
    for j in range(n):
        if check(i, j):
            cnt += 1
print(cnt)