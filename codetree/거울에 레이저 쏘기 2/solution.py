n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# 방향 벡터 정의 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 거울에 따른 방향 변화 규칙
mirror_change = {'/': {0: 1, 1: 0, 2: 3, 3: 2}, '\\': {0: 3, 1: 2, 2: 1, 3: 0}}

def find(n, k):
    if 1 <= k <= n:  # 상단
        direction = 2  # 아래쪽
        x, y = 0, k - 1
    elif n < k <= 2 * n:  # 오른쪽 
        direction = 3  # 왼쪽
        x, y = k - n - 1, n - 1
    elif 2 * n < k <= 3 * n:  # 하단
        direction = 0  # 위쪽
        x, y = n - 1, 3 * n - k
    else:  # 왼쪽
        direction = 1  # 오른쪽
        x, y = 4 * n - k, 0
    
    return direction, x, y

cnt = 0
direction, x, y = find(n, k)
while 0<=x<n and 0<=y<n: 
    direction = mirror_change[grid[x][y]][direction]
    x, y = x + dx[direction] , y + dy[direction]
    cnt +=1

print(cnt)