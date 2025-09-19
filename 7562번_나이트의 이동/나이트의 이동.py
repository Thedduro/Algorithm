#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7562                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7562                           #+#        #+#      #+#     #
#    Solved: 2025/09/19 09:01:57 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    -  문제:
        - 나이트가 이동할 수 있는 칸을 정해져있다.
        - 몇번을 이동해야, 타겟 지점으로 이동 할 수 있는지
        - N: 300
    - 시간복잡도:
        - N^2 > 체스판이 8번 연산하는건 사실상 O(1)
"""
from collections import deque
next_step = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
def bfs():
    queue = deque()
    queue.append((c_i, c_j, 0))
    board[c_i][c_j] = True

    while queue:
        x, y, time = queue.popleft()
        
        if x == t_i and y == t_j:
            return time
        
        for dx, dy in next_step:
            nx, ny = x + dx, y + dy
            if 0 > nx or nx >= N or 0 > ny or ny >= N: continue
            if not board[nx][ny]:
                queue.append((nx, ny, time+1))
                board[nx][ny] = True

T = int(input())
for tc in range(T):
    N = int(input())
    board = [[False]*N for _ in range(N)]
    c_i, c_j = map(int, input().split())
    t_i, t_j = map(int, input().split())

    print(bfs())