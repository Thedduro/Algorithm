#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10026                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10026                          #+#        #+#      #+#     #
#    Solved: 2025/09/20 20:30:24 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    -  문제:
        - 색은 RGB
            - 적록색약: R_G, B
            - 정상: R, G, B
        - 같은 색으로 이어져 있으면 , 1 구역
        - N = 100
    - IDEA:
        - 두 가지의 경우를 따로 계산
"""
from collections import deque

def R_G_B():
    R_G_B_visited = [[False] * N for _ in range(N)]
    R_G_B_value = 0
    R_G_B_queue = deque()
    for i in range(N):
        for j in range(N):
            if not R_G_B_visited[i][j]:
                R_G_B_queue.append((i,j))
                R_G_B_visited[i][j] = True
                while R_G_B_queue:
                    x, y = R_G_B_queue.popleft()
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 > nx or N <= nx or 0 > ny or N <= ny: continue
                        if R_G_B_visited[nx][ny]: continue
                        if board[nx][ny] == board[x][y]:
                            R_G_B_queue.append((nx,ny))
                            R_G_B_visited[nx][ny] = True
                R_G_B_value += 1
    return R_G_B_value

def RG_B():
    RG_B_visited = [[False] * N for _ in range(N)]
    RG_B_value = 0
    RG_B_queue = deque()
    for i in range(N):
        for j in range(N):
            if not RG_B_visited[i][j]:
                RG_B_queue.append((i,j))
                RG_B_visited[i][j] = True
                while RG_B_queue:
                    x, y = RG_B_queue.popleft()
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 > nx or N <= nx or 0 > ny or N <= ny: continue
                        if RG_B_visited[nx][ny]: continue
                        if board[x][y] in ['R','G'] and board[nx][ny] in ['R','G']:
                            RG_B_queue.append((nx,ny))
                            RG_B_visited[nx][ny] = True
                        if board[x][y] == 'B' and board[nx][ny] == 'B':
                            RG_B_queue.append((nx,ny))
                            RG_B_visited[nx][ny] = True
                RG_B_value += 1
    return RG_B_value

N = int(input())
board = [list(input()) for _ in range(N)]
direction = [(0,1),(0,-1),(1,0),(-1,0)]

print(R_G_B(), RG_B())

                