N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

import time
start = (time.time())

visited = [[False]*N for _ in range(N)]
max_value = 0

def dfs(value, k):
    global max_value

    if k == K:
        max_value = max(max_value, value)
        return

    for i in range(N):
        for j in range(N):
            # 가로
            if 0<=i<N and 0<=j and j+1<N and not visited[i][j] and not visited[i][j+1]:
                visited[i][j], visited[i][j+1] = True, True
                dfs(value + grid[i][j] + grid[i][j+1], k+1)
                visited[i][j], visited[i][j+1] = False, False
            # 세로
            if 0<=j<N and 0<=i and i+1<N and not visited[i][j] and not visited[i+1][j]:
                visited[i][j], visited[i+1][j] = True, True
                dfs(value + grid[i][j] + grid[i+1][j], k+1)
                visited[i][j], visited[i+1][j] = False, False

dfs(0,0)
print(max_value)

end = time.time()

print(end-start)