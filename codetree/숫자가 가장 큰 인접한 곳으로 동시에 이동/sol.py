'''
- 문제:
    - m개 구슬이 서로 다른 위치에서 상하좌우로 가장 큰 숫자가 있는 곳으로 이동함
    - 가장 큰 숫지가 여러개 일 경우 상하좌우 방향 순서대로 우선 이동
    - 근데 만약 동일한 곳으로 이동하면? 구슬 사라짐
    - T초 후 남아있는 구슬 개수는?
- 아이디어:
    n = 20, m = 400, T = 100
    > 완탐해도 안터짐
    - 그러면 시뮬로 풀까 BFS로 풀까?
    - 시뮬로 풀자 > 어짜피 T초 동안만 진행
    - 각 초에 구슬의 위치를 저장할 리스트를 만들고
    - 각 구슬을 이동시킴
    - 그리고 만약 겹치면 겹치는 구슬들을 삭제해
    - T초가 끝난 후 마지막 리스트의 길이를 출력
'''
n, m, t = map(int, input().split())

# Create n x n grid
grid = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
marbles = [(x-1, y-1) for x, y in marbles]
direction = [(-1,0),(1,0),(0,-1),(0,1)]

for _ in range(t):
    moves = []
    for x,y in marbles:
        max_cnt, fx,fy = 0, x, y
        for dx, dy in direction: 
            nx, ny  = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny] > max_cnt:
                max_cnt = grid[nx][ny]
                fx, fy = nx, ny
        moves.append((fx,fy))

    # 중복 제거 
    dup = {}
    for move in moves:
        if move not in dup.keys():
            dup[move] = 1
        else:
            dup[move] += 1
    arr = []
    for key, cnt in dup.items():
        if cnt >= 2:
            continue
        else:
            arr.append(key)
    marbles = arr
    
print(len(marbles))
