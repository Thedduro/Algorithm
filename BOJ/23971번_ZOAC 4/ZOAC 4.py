'''
- 문제
    - 테이블이 H*W개, 각 테이블은 한명씩만 앉을 수 있음
    - 모든 사람은 세로 N칸 또는 가로 M칸 이상 비우고 앉아야 함
    (모든 참가자와 세로줄 번호의 차 >= N, 가로줄 번호의 차가 >= M)
    - 최대 몇명 가능?
- 아이디어
    - 우선 첫번째 칸에 무조건 사람을 앉히고
    - 가로 M, 세로 N 만큼 떨어진 곳에 사람 앉힘.
    - BFS > 큐
'''
# from collections import deque

# H, W, N, M = map(int, input().split())
# tables = [[False]*W for _ in range(H)]

# queue = deque([])
# queue.append((0,0))

# cnt = 0
# direction = [[0,M+1], [N+1,0]]
# while queue:
#     x, y = queue.popleft()
    
#     if tables[x][y]: # 만약 테이블에 이미 사람이 앉아 있으면
#         continue

#     tables[x][y] = True
#     cnt += 1

#     for dir in direction:
#         nx, ny = x+dir[0], y+dir[1]
#         if 0<=nx<H and 0<=ny<W:
#             queue.append((nx, ny))

# print(cnt)

H, W, N, M = map(int, input().split())

row = (H + (N + 1) - 1) // (N + 1)
col = (W + (M + 1) - 1) // (M + 1)

print(row*col)