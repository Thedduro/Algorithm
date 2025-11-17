'''
- 문제:
    - 바라보는 방향이 벽일때, 반시계 방향으로 방향 바꿈
    - 범위 밖을 벗어날 수 있는 경우 탈출이라 함
    - 방향으로 이동 했는데, 오른쪽에 벽이 없을 경우 > 시계 방향으로 방향 바꿔서 한 칸이동
    (즉, 오른쪽에 벽이 있게함)
    - 방향 트는데 시간 x, 이동하는데 1초 시간, 총 시간은? 불가일 경우 -1 출력

- 아이디어: 
    - 만약, 한번 들렸던 위치로 같은 방향으로 들어온다면, 탈출 불가 선언
    - 큐에 x,y,'R'를 넣고 큐가 끝날때까지 cnt up
    - 우선 오른쪽에 벽이있으면 일단 앞으로 움직인다. 
        - 그리고 움직인 위치에서 오른쪽에 벽이 있으면 다시 앞으로 이동
        - 벽이 없다면? 다음 방향으로 봄
'''
from collections import deque

N = int(input())
x, y = map(int, input().split())
x, y = x-1, y-1
grid = [list(map(str,input())) for _ in range(N)]

queue = deque([])
queue.append((x, y, 'R'))
visited = set()
cnt = 0

def check(x,y,dir): # 오른쪽에 벽이 있는지 없는지 확인
    if dir == 'U':
        x, y = x, y+1
    if dir == 'D':
        x, y =  x, y-1
    if dir == 'L':
        x, y = x-1, y
    if dir == 'R':
        x, y = x+1, y
    if grid[x][y] == '#':
        return True
    return False

direction = {'U':[(-1,0), 'L',(0,1), 'R'], 'D':[(1,0),'R',(0,-1),'L'], 'L':[(0,-1),'D',(-1,0),'U'], 'R':[(0,1),'U',(1,0),'D']}
flag = True
while queue:
    x, y, dir = queue.popleft()

    if (x,y,dir) in visited:
        print(-1)
        flag = False
        break
    visited.add((x,y,dir))

    dx, dy = direction[dir][0]
    nx, ny = x+dx, y+dy

    if not(0<=nx<N and 0<=ny<N):
        cnt += 1
        break
    if grid[nx][ny] == '#':
        queue.append((x,y,direction[dir][1]))
        continue

    if check(nx,ny,dir):
        queue.append((nx,ny,dir))
        cnt += 1

    else:
        ddx, ddy = direction[dir][2]
        nnx, nny = nx + ddx, ny+ddy
        queue.append((nnx, nny, direction[dir][3]))
        cnt += 2
if flag:
    print(cnt)