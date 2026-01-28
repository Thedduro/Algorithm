'''
문제:
    - 1: 벽, 0: 청소 x
    - 유형
        1. 청소안되어 있음, 청소
        2. 주변 4칸이 모두 청소되어있으면
            1. 한칸 후진할 수 있으면 후진 > while
            2. 후진 불가 -> 작동 중단
        3. 주변 4칸 중 청소되지 않은 칸 존재
            1. 반시계 방향 90도 회전
            2. 앞 칸이 청소되지 않으면 전진 > while
            3. 청소되어있으면 90도 회전돌아감. 
    - 작동을 멈출 때까지 청소하는 칸의 개수는?

아이디어:
    - 우선 방향당 이동 방향 리스트, 방향당 반대 90도 반대 방향을 정의할 수 있어야 함.
    - while 문으로 계속 돌림. 
    - 예외 케이스 처리해서 반복
    - cnt는 칸을 청소할때마다 바로 카운트 업
    - 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다.?
'''

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
dir = [(-1,0),(0,1),(1,0),(0,-1)]
# 북(0) > 서(3), 동(1) > 북(0), 남(2) > 동(1), 서(3) > 남(2) # 90도 회전
# 북(0) > 남(2), 동(1) > 서(3), 남(2) > 북(0), 서(3) > 동(1) # 한칸 후진

while True:
    if board[x][y] == 0:
        cnt += 1
        board[x][y] = -1 # 청소 처리
        print(x, y, d)
    
    if board[x-1][y] != 0 and board[x][y+1] != 0 and board[x+1][y] != 0 and board[x][y-1] != 0: # 4칸을 모두 청소할수 없음
        back = (d + 2) % 4  
        dx, dy = dir[back]
        nx, ny = x + dx, y + dy
        if board[nx][ny] != 1: # 후진 가능
            x, y = nx, ny
            continue
        else:
            break

    else:
        while True:
            d = (d+3) % 4
            dx, dy = dir[d]
            nx, ny = x + dx, y + dy
            if board[nx][ny] == 0:
                x, y = nx, ny
                continue

print(cnt)