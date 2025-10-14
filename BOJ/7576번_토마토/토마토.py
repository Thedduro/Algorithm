#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7576                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7576                           #+#        #+#      #+#     #
#    Solved: 2025/09/18 08:59:40 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    - 문제: 
        - 인접한 토마토는 익은 토마토의 영향을 받아 익게 됨
        - 모두 익을때까지 최소 날짜 구하라
        - 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 없음
        - 원래 모든 토마토가 익어있으면 0 출력, 토마토가 모두 익을 수가 없으면 -1 출력
        - N = 1,000
    - IDEA:
        - 우선 익은 토마토들의 위치를 큐에 삽입
        - 큐를 돌면서 인접한 토마토를 2, 3, 이럴게 시간으로 바꿈
            - 어짜피 0만 바꿀수 있음
        - 그러다가 모든 큐가 끝나면 모든 토마토 판을 돌면서 최소 값을 검사.
            - -1을 제외하고 0이 있으면 > 모든 토마토가 익을 수 없다
            - -1, 0이 없고 최소 값이 최소 날짜
"""
from collections import deque
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

origin_tomato = []
tomato = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            tomato.append((i,j,0))
            origin_tomato.append([i,j])

direction = [(0,1),(0,-1),(1,0),(-1,0)]
while tomato:
    x, y, time = tomato.popleft()

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= N or 0 > ny or ny >= M: continue
        if board[nx][ny] == -1: continue
        if board[nx][ny] == 0: # 안익은 토마토만
            board[nx][ny] = time + 1
            tomato.append((nx, ny, time+1))

def find():
    result = 0
    for i in range(N):
        for j in range(M):
            if  board[i][j] == 0:
                return -1
            elif result < board[i][j] and [i,j] not in origin_tomato:
                result = board[i][j]
    return result

print(find())