'''
- 문제:
    - N개의 숫자 세트 > M개의 숫자 존재(중복 숫자 가능)
    - 0부터 9까지 숫자 퍼즐을 모으기 위한 최소한의 퍼즐 세트 개수
    - N = 20, M=10
- 아이디어: 
    - 일단 각 퍼즐을 정렬하고
    - 각 세트에서 필요한 숫자를 찾기
        - 
    - 필요한 숫자가 적은 퍼즐부터 사용...
    > 만족하면 세트의 개수를 줄여보기,,
    > 만족하지 않으면 세트의 개수 늘려

'''
from collections import deque

N, M = map(int, input().split())
puzzles = [list(map(int, input().split())) for _ in range(N)]

masks  = []
# 비트마스크로 변환
for puzzle in puzzles:
    mask = 0
    for x in puzzle:
        mask |= (1<<x) # or 대입 후 연산
    masks.append(mask)

target = (1<<10) - 1 # 1023

queue = deque()
visited = [False]  * (1<<10)
queue.append((0,0)) # (현재 마스크, 사용한 세트 개수)
visited[0] = True

while queue:
    curr, cnt = queue.popleft()

    if curr == target:
        print(cnt)
        break

    for mask in masks:
        new = curr | mask
        if not visited[new]:
            visited[new] = True
            queue.append((new, cnt + 1))
