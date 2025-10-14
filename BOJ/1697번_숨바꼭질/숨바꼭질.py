#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1697                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1697                           #+#        #+#      #+#     #
#    Solved: 2025/09/18 16:39:34 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    - 문제:
        - 수빈이는 -1, +1 또는 순간이동(2*X)로 이동가능
        - 동생이 K일때 얼마나 빠른 시간으로 찾을 수 있는지 구해라
        - N = 100,000
    - IDEA:
        - BFS로 접근하기
        - visited 는 set으로 수빈이의 위치 저장 > 이미 간 곳은 다시 갈 필요 없음
        - 위치를 찾으면, 그때의 값을 출력
        - set에사 값을 찾는 것 > O(1) 시간복잡도
"""
from collections import deque
N, K = map(int, input().split())

queue = deque()
visited = set()

queue.append((N, 0))
visited.add(N)

MAX = 100000

while queue:
    n, time = queue.popleft()

    if n == K: # 찾았다 
        print(time)
        break

    if n < 0: continue

    if n-1 not in visited and 0 <= n-1 <= MAX: 
        queue.append((n-1, time+1))
        visited.add(n-1)
    if n+1 not in visited and 0 <= n+1 <= MAX: 
        queue.append((n+1, time+1))
        visited.add(n+1)
    if n*2 not in visited and 0 <= n*2 <= MAX:
        queue.append((n*2, time+1))
        visited.add(n*2)