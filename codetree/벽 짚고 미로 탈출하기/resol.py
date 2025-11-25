'''
- 문제:
    - 가는 방향에 벽
    - 
'''
from collections import deque

N = int(input())
x, y = map(int, input().split())
x, y = x-1, y-1
grid = [list(map(str,input())) for _ in range(N)]

direction = {'U':[(-1,0), 'L',(0,1), 'R'], 'D':[(1,0),'R',(0,-1),'L'], 'L':[(0,-1),'D',(-1,0),'U'], 'R':[(0,1),'U',(1,0),'D']}

queue = deque([])
queue.append((x, y, 'R', 0))

visited = set()

while queue:
    x, y, dir, cnt = queue.popleft()
    
    if (x,y,dir) in visited:
        cnt = -1
        break

    visited.add((x, y, dir))    
    
    dx, dy = direction[dir][0]
    nx, ny = x+dx, y+dy

    if 0<=nx<N and 0<=ny<N:
        if grid[nx][ny] == '#': # 벽 > 반시계 방향회전
            queue.append((x,y,direction[dir][1] ,cnt))
        else:
            nnx, nny = nx + direction[dir][2][0], ny + direction[dir][2][1]
            if grid[nnx][nny] == '#': # case2
                queue.append((nx,ny,dir,cnt+1))
            else: # case3
                new_dir = direction[dir][3]
                new_x, new_y = direction[new_dir][0]
                nx, ny = nx + new_x, ny + new_y
                queue.append((nx,ny,new_dir,cnt+2))
        
    else: # Case1 탈출
        cnt += 1
        break    
    
print(cnt)