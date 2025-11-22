'''
- 문제:
    - 구슬마다 이동 거리, 이동 방향이 있는데
    > 벽에 부딪히면, 남은 이동 거리만큼 더 감
    - 같은 위치에 위치한 구슬이 K개 이하면 아무일도 안일어남.
    - 그넫 만약, K가 넘으면, 우선순위가 높은 K개만 (이동거리가 높은)
    - 구슬의 이동거리가 높으면, 구슬의 번호가 더 높은 구슬이 우선순위가 더 높음
    - T초가 지난 이후 구슬의 개수?
- 아이디어:
    - 리스트에 추가하면서 만약에 같은 
'''

n, m, t, k = map(int, input().split())


marbles =[]
for i in range(1, m+1):
    r,c,dir,v = input().split()
    marbles.append((int(r)-1,int(c)-1,dir,int(v),i))

direction = {
    'L': ((0, -1), 'R'),
    'R': ((0, 1), 'L'),
    'U': ((-1, 0), 'D'),
    'D': ((1, 0), 'U')
}

def moving(x, y, dir, v, i):
    dx, dy = direction[dir][0]
    L = n - 1
    cycle = 2 * L

    # x축 이동
    if dx != 0:
        raw = x + dx * v
        moved = raw % cycle
        nx = moved if moved <= L else cycle - moved
        
        # 반사 횟수 = raw // L
        reflect_count = raw // L

        if reflect_count % 2 == 0:
            new_dir = dir
        else:
            new_dir = direction[dir][1]

        return (nx, y, new_dir, v, i)

    # y축 이동
    else:
        raw = y + dy * v
        moved = raw % cycle
        ny = moved if moved <= L else cycle - moved

        reflect_count = raw // L
        
        if reflect_count % 2 == 0:
            new_dir = dir
        else:
            new_dir = direction[dir][1]

        return (x, ny, new_dir, v, i)

def check(moves):
    grid = [[[] for _ in range(n)] for _ in range(n)]
    for x, y, dir, v, i in moves:
        grid[x][y].append((dir,v,i))
    
    result = []
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                grid[i][j].sort(key=lambda x: (x[1], x[2]), reverse=True)
                for dir,v,idx in grid[i][j][:k]:
                    result.append((i,j,dir,v,idx))
    return result


for _ in range(t):
    moves = []

    for x, y, dir, v, i in marbles:  
        next = moving(x, y, dir, v, i)
        moves.append(next)
    
    marbles = check(moves)

print(len(marbles))
