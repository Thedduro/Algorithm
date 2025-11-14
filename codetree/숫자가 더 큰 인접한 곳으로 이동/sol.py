n, r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
r, c = r-1, c-1

from collections import deque

queue = deque([])
queue.append((board[r][c],r,c))

direction = [(-1,0),(1,0),(0,-1),(0,1)]

result = []
result.append(board[r][c])
while queue:
    num, x, y = queue.popleft()

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > num:
            result.append(board[nx][ny])
            queue.append((board[nx][ny], nx, ny))
            break

print(*result)