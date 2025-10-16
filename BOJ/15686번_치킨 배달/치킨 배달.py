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

'''
- 문제:
    - 집과 가까운 치킨집의 거리 > 도시의 치킨거리: 총합
    - M개만 남기고 치킨집을 폐업 > 도시 치킨거리의 최소값은?
    - 시간제한: 1억 , N = 50 > 2500, M = 13
- 구현:
    1. 각 집에서 각 치킨 집 거리을 구함
    2. BFS로 치킨집 인덱스의 조합을 구함
    3. 만약 조합의 개수가 M과 같다면? 총 도시의 거리 계산
    4. 최소값 갱신으로 정답 찾기
'''

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨의 위치 정보
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i,j))

# 이제 거리 계산
weights = {} 
for h in house:
    for c in chicken:
        weight = abs(h[0]-c[0]) + abs(h[1]-c[1])
        if h not in weights.keys():
            weights[h] = [weight]
        else:
            weights[h].append(weight) 
#{(0, 3): [2, 6, 7, 6, 5], (1, 0): [2, 2, 3, 4, 7], (1, 2): [2, 4, 5, 4, 5], (3, 3): [5, 3, 4, 3, 2], (3, 4): [6, 4, 5, 4, 1], (4, 3): [6, 4, 3, 2, 1]}

# BFS : 이제 모든 M개의 조합을 구함
queue = [([], 0)]
min_distance = float('inf')

while queue:
    selected, start = queue.pop()

    if len(selected) == M: # 모든 조합이 완성됐을때
        total = 0
        for distances in weights.values():
            min_value = N*N
            for s in selected:
                if min_value > distances[s]:
                    min_value = distances[s]
            total += min_value
        if total < min_distance:
            min_distance = total
            continue

    for i in range(start, len(chicken)):
        queue.append((selected + [i], i+1))
        
print(min_distance)