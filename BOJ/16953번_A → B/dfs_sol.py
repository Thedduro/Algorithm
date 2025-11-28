a, b = map(int, input().split())
min_cnt = float('inf')

visited = set()

def dfs(value, cnt):
    global min_cnt

    if cnt >= min_cnt:
        return
    
    if value == b:
        min_cnt = min(min_cnt, cnt)
        return
    
    if value > b:
        return
    
    # 2를 곱하는 연산
    if value*2 not in visited:
        visited.add(value*2)
        dfs(value*2, cnt+1)
    # 1를 추가하는 연산
    next_value = int(str(value)+'1')
    if next_value not in visited:
        visited.add(next_value)
        dfs(next_value, cnt+1)

visited.add(a)
dfs(a, 0)

if min_cnt != float('inf'):
    print(min_cnt+1)
else:
    print(-1)