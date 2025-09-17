"""
    - 문제:
        - 불은 상하좌우로 확대 (벽 x)
        - 상근이는 상하좌우 인접 칸으로 이동 가능 (벽 통과 x, 불 칸 이동 x)
        - 상근이가 있는 칸에 불이 오는 동시에 다른 칸으로 이동은 가능
        - 얼마나 빨리 탈출 가능한지 풀어라
    - IDEA:
        - T = 100
        - N = 100 > 10,000
        - BFS를 두번 돌릴거임
        - 1. 불이 퍼지는 시간을 또다른 자료 구조에 기록
        - 2. 상근이 퍼지는데, 상근이가 가는 시간보다 불의 도달시간이 크면 이동가능
            - 2.1 범위를 벗어나면 이동가능
            - 2.2 BFS가 다 끝날때까지 탈출 못해? > 불가
"""
from collections import deque

direction = [(0,1),(0,-1),(1,0),(-1,0)]

def fire_bfs():
    INF = 10**9
    fire_map = [[INF] * w for _ in range(h)]
    
    while fire_queue:
        x, y, time = fire_queue.popleft() 
        fire_map[x][y] = time
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy 
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue 
            if board[nx][ny] == '#':
                continue
            if fire_map[nx][ny] != INF: # 이미 불이 번진경우 > 즉 방문한 경우 
                continue
            else:
                """
                    큐에 넣기 전에 방문처리를 또 하는 이유:
                        - (nx,ny)가 아직 INF라서 조건을 통과 → 큐에 들어감.
                        - 다른 경로에서도 같은 칸 (nx,ny)를 확인 → 여전히 INF이므로 또 큐에 들어감.
                        - 결국, (nx,ny) 좌표가 큐에 여러 번 들어가게 됨. → 큐가 급격하게 증가하여, 메모리 사용량이 급증한다.
                """
                fire_map[nx][ny] = time+1  # 큐 넣기 전에 방문 처리
                fire_queue.append((nx, ny, time + 1))
    return fire_map


def survivor_bfs(fire_map):
    visited = [[False] * w for _ in range(h)]
    f_x, f_y, t = survivor[0]
    visited[f_x][f_y] = True

    while survivor:
        x, y, time = survivor.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= h or ny >= w: # 상근이가 범위를 넘으면? 탈출 가능
                    return time+1
            if board[nx][ny] == '#':
                continue
            if visited[nx][ny]:
                continue
            if fire_map[nx][ny] > time+1: # 불이 도달한 시간보다 상근이가 가는 시간이 더 짧으면
                visited[nx][ny] = True
                survivor.append((nx, ny, time+1))
   
    # 다끝났는데? 리턴을 안했잖아? > 탈출 불가
    return False

T = int(input())
for _ in range(T): 
    w, h = map(int, input().split())
    board = [input().strip() for _ in range(h)]
    
    fire_queue = deque()
    survivor = deque()
    
    # 불의 시작 위치를 큐에 삽입
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire_queue.append((i,j,0)) # 위치와 시간 삽입
            if board[i][j] == '@':
                survivor.append((i,j,0))

    value = survivor_bfs(fire_bfs())
    
    if not value:
        print("IMPOSSIBLE")
    else:
        print(value)
