'''
- 문제:
    - 모든 구슬은 1초에 한칸씩 정해진 방향으로 이동
    - 벽에 부딪히면, 방향을 바꿈 (여기에도 1초 소요)
    - 움직이고 구슬의 위치가 겹치면 구슬이 사라짐
    - 아주 오랜 시간이 지난 뒤에도..?
- 아이디어:
    - 우선 모든 구슬을 돌면서, 위치와 방향을 업뎃 
    - 그리고 중복 구슬을 제거한다.
    - 그래서 몇번을 도는 건, 패턴을 찾아야 함.
- 시간복잡도:
    - t = 100, n= 50, m=N*N 
    - 중복제거를 위한 반복문 > 여기서 계속 시간초과
    - 2차원 배열로 구슬의 위치를 관리하자,,,, > 그냥 구슬을 한번씩 돌면서 아예 그쪽으로 가게 되면 둘다 터지는 ..
'''

direction = {
    'L': ((0, -1), 'R'),
    'R': ((0, 1), 'L'),
    'U': ((-1, 0), 'D'),
    'D': ((1, 0), 'U')
}

def move(marbles, N):
    moved = []
    for x, y, d in marbles:
        (dx, dy), bounce = direction[d]
        nx, ny = x + dx, y + dy

        if not (0 <= nx < N and 0 <= ny < N):
            nx, ny = x, y
            d = bounce

        moved.append((nx, ny, d))
    return moved


def check(moved, N):
    # 2D 배열로 충돌 카운트
    count = [[0] * N for _ in range(N)]

    # 충돌 카운트
    for x, y, d in moved:
        count[x][y] += 1

    new_marbles = []

    for x, y, d in moved:
        if count[x][y] == 1:   # 단 하나만 있으면 생존
            new_marbles.append((x, y, d))

    return new_marbles


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    marbles = []

    for _ in range(M):
        x, y, d = input().split()
        marbles.append((int(x)-1, int(y)-1, d))

    for _ in range(N * 2):
        moved = move(marbles, N)
        marbles = check(moved, N)

    print(len(marbles))

    # for _ in range(N*2):
    #     move = {}
    #     for x, y, dir in marbles:
    #         dx, dy = direction[dir][0]
    #         nx, ny = x+dx, y+dy
    #         if 0<=nx<N and 0<=ny<N and (nx,ny) not in move:
    #             move[(nx,ny)] = [1, dir]
                
    #         elif not (0<=nx<N and 0<=ny<N) and (x,y) not in move:
    #             move[(x,y)] = [1, direction[dir][1]]
            
    #         elif 0<=nx<N and 0<=ny<N and (nx,ny) in move:
    #             move[(nx,ny)][0] += 1
            
    #         elif not (0<=nx<N and 0<=ny<N) and (x,y) in move:
    #             move[(x,y)][0] += 1

    #     marbles = [(x, y, d) for (x, y), (c, d) in move.items() if c == 1]

        # # 중복제거
        # dup_cnt = {}
        # dup_dir = {}
        # for x,y,dir in moves:
        #     key = (x,y)
        #     if key in dup_cnt:
        #         dup_cnt[key] += 1
        #     else:
        #         dup_cnt[key] = 1
        #         dup_dir[key] = dir

        # arr = []
        # for (x,y), cnt in dup_cnt.items():
        #     if cnt == 1:
        #         arr.append((x,y,dup_dir[(x,y)]))
        # marbles = arr