n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r)-1, int(c)-1

direction = {'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}
next_direction = {'U':'D','D':'U','R':'L','L':'R'}

for _ in range(t):
    dx, dy = direction[d]
    nr, nc = r+dx, c+dy
    if 0 <= nr < n and 0 <= nc < n:
        r, c = nr, nc
    else:
        d = next_direction[d]

print(r+1, c+1)