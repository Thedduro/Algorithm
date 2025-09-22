#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2468                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2468                           #+#        #+#      #+#     #
#    Solved: 2025/09/21 23:17:03 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    - 문제: 
        - 안전지역을 최대 수로 만드는 물의 높이를 구해라
        - N = 100 > 10,000
"""

from collections import deque
direction = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(n):
    visited = [[False] * N for _ in range(N)]
    safety = 0

    for x in range(N):
        for y in range(N):
            if n == 27:
                print(x,y,board[x][y])
            if not visited[x][y] and board[x][y] > n:
                
                queue = deque()
                queue.append((x, y))
                visited[x][y] = True

                while queue:
                    xx, yy = queue.popleft()
                    for dx, dy in direction:
                        nx , ny = xx + dx, yy + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and board[nx][ny] > n:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                safety += 1
                
    return safety, visited

N = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(N)]
print(board)
min_height, max_height = 100, 0
for i in range(N):
  for j in range(N):
    if board[i][j] > max_height:
      max_height = board[i][j]
    if board[i][j] < min_height:
      min_height = board[i][j]
      
value = 1

for i in range(max_height):
    safety, visited = bfs(i)
    if safety > value: 
        # print(i, safety, visited)
        value = safety
        
print(value)
