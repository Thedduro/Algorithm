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
            if not visited[x][y] and board[x][y] > n:
                queue = deque()
                queue.append((x, y))
                visited[x][y] = True

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in direction:
                        nx , ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and board[nx][ny] > n:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                safety += 1
    return safety

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, board))  # 입력값에서 가장 높은 지점까지만 검사
min_height = min(map(min, board))
value = 0

for i in range(min_height, max_height + 1):
    safety = bfs(i)
    if safety > value: 
        value = safety
print(value)
