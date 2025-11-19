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
'''
direction = {'L':[(0,-1),'R'],'R':[(0,1),'L'],'U':[(-1,0),'D'],'D':[(1,0),'U']}
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    marbles = []
    for _ in range(M):
        xi, yi, di = input().split()
        marbles.append((int(xi),int(yi),di))

    for _ in range(N*N):
        moves = []
        for x, y, dir in marbles:
            dx, dy = direction[dir][0]
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                moves.append((nx,ny,dir))
            else:
                moves.append((x,y,direction[dir][1]))
        # 중복제거
        dup = {}
        for x,y,dir in moves:
            if (x,y) in dup.keys():
                dup[(x,y)] += 1
            else:
                dup[(x,y)] = 1
        arr = []
        for key, cnt in dup.items():
            if cnt >= 2:
                continue
            else:
                arr.append(key)
        print(arr)