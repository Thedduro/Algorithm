from collections import deque

a, b = map(int, input().split())
min_cnt = float('inf')

queue = deque()
queue.append((a, 0))

visited = set()
visited.add(a)

while queue:
    value, cnt = queue.popleft()

    if cnt >= min_cnt:
        continue

    if value == b:  
        min_cnt = min(min_cnt, cnt)
        continue

    if value > b:
        continue
    
    if value*2 not in visited:
        visited.add(value*2)
        queue.append((value*2, cnt+1))
    
    if value * 10 + 1 not in visited:
        visited.add(value * 10 + 1)
        queue.append((value * 10 + 1, cnt+1))

if min_cnt != float('inf'):
    print(min_cnt+1)

else:
    print(-1)