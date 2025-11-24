'''
- 문제:
    - 1*2, 2*1 블럭을 겹치지 않게 K개 잡아서, 동전의 개수를 최대로 해라
- 아이디어:
    - dfs 구현
        pos = 0  → (0,0)
        pos = 1  → (0,1)
        pos = 2  → (0,2)
        pos = 3  → (1,0)

'''

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0
visited = [[False] * N for _ in range(N)]

def dfs(pos, cnt, k):
    global max_cnt

    if k == K:
        max_cnt = max(max_cnt, cnt)
        return
    
    if pos == N*N:
        return 
    
    x, y = pos//N, pos%N

    # 이미 사용된 칸? > 다음 칸으로 넘어감
    if visited[x][y]:
        dfs(pos + 1, cnt, k)
        return
    
    # 가로
    if y + 1 < N and not visited[x][y+1]:
        visited[x][y], visited[x][y+1] = True, True
        dfs(pos+1, cnt + grid[x][y] + grid[x][y+1], k+1)
        visited[x][y], visited[x][y+1] = False, False

    # 세로
    if x + 1 < N and not visited[x+1][y]:
        visited[x][y], visited[x+1][y] = True, True
        dfs(pos+1, cnt + grid[x][y] + grid[x+1][y], k+1)
        visited[x][y], visited[x+1][y] = False, False
    
    # 이건 블록 아예 안세웠을때
    dfs(pos+1, cnt, k)

dfs(0,0,0)
print(max_cnt)
