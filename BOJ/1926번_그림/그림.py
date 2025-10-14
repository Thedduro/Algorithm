"""
    - 문제:
        - 1로 연결되어 있는 그림의 개수, 그림의 크기 중 최대 값을 구해라.
        - 상하좌우로만 이동 가능. 한 노드에 다시 갈 이유는 전혀 없다
        - N = 500 > 완탐시 250,000
    - IDEA:
        - BFS로 풀어본다. (왜냐하면, 연습해야 하니까!!!!!!!)
        - visited를 사용해, 한번 간 곳은 다시 가지는 않는다
        - 0이거나, 배열을 넘어간 경우 가지 않는다. 
"""
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1,0), (1,0), (0,-1),(0,1)]

paint_cnt = 0
max_cnt = 0
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
         # 그림이고, 방문을 안했으면 그림으로 판단 > 크기를 계산
        if board[i][j] == 1 and not visited[i][j]:
            queue = deque()
            queue.append((i,j))

            visited[i][j] = True
            current_cnt = 1 # 현재 그림의 크기

            while queue:
                x, y = queue.popleft()

                for dx, dy in direction:
                    nx, ny = x + dx, y + dy

                    # 패스 조건
                    if 0 > nx or N <= nx or 0 > ny or M <= ny: continue
                    if visited[nx][ny]: continue
                    if board[nx][ny] == 0: continue
                    
                    # 그림완성 조건
                    else: 
                        visited[nx][ny] = True 
                        queue.append((nx,ny)) 
                        current_cnt += 1 # 그림 크기 증가

            # While을 빠져나온다 > 해당 그림이 끝남(더이상 갈 곳이 없음)
            paint_cnt += 1 # 하나의 그림이 완성
            if max_cnt < current_cnt: # 해당 그림의 크기가 최대치를 갱신하면
                max_cnt = current_cnt

# 출력
print(paint_cnt)
print(max_cnt)