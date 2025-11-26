from collections import deque

N = int(input())
x, y = map(int, input().split())
x, y = x-1, y-1
grid = [list(map(str,input())) for _ in range(N)]

direction = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}

queue = deque([(x, y, 'R', 0)])

def check(x, y):
    if 

def sol():
    x, y, dir, cnt = queue.popleft()
