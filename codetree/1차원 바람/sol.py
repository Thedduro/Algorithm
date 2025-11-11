n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r)-1, d) for r, d in [input().split() for _ in range(q)]]

'''
    - 문제: 
        - 한쪽 방향으로 한칸씩 밀림. > 위 아래도 전파됨 (반대 방향)
        - 전파 조건
            - 현재 행과 전파 행의 같은 열에 같은 숫자가 있다면
        - 바람 끝 조건, 1. 같은 숫자가 아예 없어, 또는 더 전파할 곳이 없어
    - 아이디어:
        - BFS로 행의 인덱스, 방향정보를 넣고, 조건을 통과하면 (같은 숫자가 있는지, 범위 안인지)
            - 인덱스 +1과 -1을 넣고 반대방향을 정의해서 넣음, 그리고 visited 추가
    - 시간복잡도:
        - 100*100 
        - wind는 100
        > 내 풀이는 100^3
'''
from collections import deque

direction =  {'L': 'R', 'R': 'L'}

for wind in winds:
    queue =  deque()
    queue.append(wind)
    visited = set()

    while queue:
        idx, dir = queue.popleft()
        arr = deque(a[idx])
        if dir == 'L':
            arr.rotate(1) # 맨 뒤 원소 하나를 앞으로
        if dir == 'R':
            arr.rotate(-1) # 맨 앞 원소 하나를 뒤로
        a[idx] = list(arr) # 바람 불어서 이동
        visited.add(idx)

    # 전파 조건 확인
        # 위쪽 방향 확인
        if 0 <= idx-1 and idx-1 not in visited:
            # 각 열에 맞는 숫자가 있는지 확인
            flag = False
            for i in range(m):
                if a[idx-1][i] == a[idx][i]:
                    flag = True
                    break
            if flag:
                queue.append((idx-1, direction[dir]))
                
        # 아래쪽 방향 확인
        if idx+1 < n and idx+1 not in visited:
            flag = False
            for i in range(m):
                if a[idx][i] == a[idx+1][i]:
                    flag = True
                    break
            if flag:
                queue.append((idx+1, direction[dir]))

for arr in a:
    print(*arr)