n, m, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r)-1, d) for r, d in [input().split() for _ in range(q)]]

from collections import deque

for i, dir in winds:
    queue = deque()
    queue.append((i,dir))
    visited = set()
    visited.add(i)

    while queue:
        i, dir = queue.popleft()
        row = deque(board[i])
        if dir == 'L':
            row.rotate(1)
            n_dir = 'R'
        else:
            row.rotate(-1)
            n_dir = 'L'
        board[i] = row

        if 0<= i-1 and i-1 not in visited:
            for j in range(m):
                if row[j] == board[i-1][j]:
                    queue.append((i-1, n_dir))
                    visited.add(i-1)
                    break
        if i+1<n and i+1 not in visited:
            for j in range(m):
                if row[j] == board[i+1][j]:
                    queue.append((i+1, n_dir))
                    visited.add(i+1)
                    break

for row in board:
    print(*row)