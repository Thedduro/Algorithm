n = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n   # 열 사용 여부
answer = -1             # 최솟값들 중 최댓값

def dfs(row, cur_min):
    global answer

    # n개의 행에서 모두 하나씩 골랐으면 결과 갱신
    if row == n:
        if cur_min > answer:
            answer = cur_min
        return

    # 현재 row에서 어떤 열을 고를지
    for col in range(n):
        if visited[col]:
            continue

        visited[col] = True
        new_min = min(cur_min, grid[row][col])
        dfs(row + 1, new_min)
        visited[col] = False

dfs(0, float('inf'))
print(answer)
