#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15686                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207@gmail.com <boj.kr/u/lsw2207@gmail   +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15686                          #+#        #+#      #+#     #
#    Solved: 2025/10/16 09:17:24 by lsw2207@gmail.###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city [i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

# print(house, chicken) 
# [(0, 2), (1, 4), (2, 1), (3, 2)] [(1, 2), (2, 2), (4, 4)]

weights = {}
for c in chicken:
    for h in house:
        weight = abs((c[0]-h[0])) + abs(c[1]-h[1])
        if h in weights.keys():
            weights[h].append(weight)
        else:
            weights[h] = [weight]

# print(weights) 
# {(0, 2): [1, 2, 6], (1, 4): [2, 3, 3], (2, 1): [2, 1, 5], (3, 2): [2, 1, 3]}

# 이제 치킨집의 조합을 구해야함
from collections import deque
queue = deque([([], 0)])
min_weight = float('inf')

while queue:

    idx, start = queue.popleft()

    if len(idx) == M:
        sum = 0
        for item in weights.values():
            min_sum = float('inf')
            for i in idx:
                if min_sum > item[i]:
                    min_sum  = item[i]
            sum += min_sum
        min_weight  = min(min_weight, sum)
        continue
    
    for i in range(start, len(chicken)):
        queue.append((idx + [i], i+1))

print(min_weight)