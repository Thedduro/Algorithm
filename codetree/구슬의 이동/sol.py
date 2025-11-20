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
    marbles.append((r,c,dir,v,i))

direction = {
    'L': ((0, -1), 'R'),
    'R': ((0, 1), 'L'),
    'U': ((-1, 0), 'D'),
    'D': ((1, 0), 'U')
}

def moving(x, y, dir, v, i):
    dx, dy = direction[dir]
    nx, ny = x + (dx*v), y + (dy*v)
    if 0 <= nx < n and 0 <= ny < n:
        return (nx, ny, dir, v, i)
    else:
        
for _ in range(t):
    move = []

    for x, y, dir, v, i in marbles:
        dx, dy = direction[dir]
        nx, ny = x + (dx*v), y + (dy*v)
        if 0 <= nx < n and 0 <= ny < n:
            
        next = moving(x, y, dir, v)