#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2178                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2178                           #+#        #+#      #+#     #
#    Solved: 2025/09/17 12:10:06 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
    - 문제: 
        - (1,1) -> (N,M)으로 가는 최단 경로를 구해라
        - N = 100 
    - IDEA:
        - 두가지 방법으로 풀수 있음 1. 최단경로(dijkstra) 2. BFS
        - BFS 방법으로 먼저 풀어보자.
"""

from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]


def bfs():
    queue = deque()
    queue.append((0,0,1))
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True

    min_weight = 10**9
    
    while queue:
        x, y, weight = queue.popleft()
        
        # 도착지점에 도착했을때
        if x == N-1 and y == M-1:
            if weight < min_weight:
                min_weight = weight
                continue

        # 이후 방문
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if board[nx][ny] == 0: continue # 이동불가
            if visited[nx][ny]: continue
            else: 
                queue.append((nx, ny, weight+1))
                visited[nx][ny] = True

    return min_weight
print(bfs())