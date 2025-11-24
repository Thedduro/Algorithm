# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]
visited_pos = []
max_sum = 0

# 주어진 위치에 대하여 가능한 모든 모양을 탐색하며 최대 합을 반환합니다.
def get_max_sum(cnt, sum_of_nums):
    global direction
    global max_sum
    
    if cnt == 5:
        max_sum = max(max_sum, sum_of_nums)
        return
    
    for (x, y) in visited_pos:
        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited_pos:
                visited_pos.append((nx, ny))
                get_max_sum(cnt + 1, sum_of_nums + grid[nx][ny])
                visited_pos.pop()


# 격자의 각 위치에 대하여 탐색해줍니다.
for i in range(n):
    for j in range(m):
        visited_pos.append((i, j))
        get_max_sum(1, grid[i][j])
        visited_pos.pop()

print(max_sum)
