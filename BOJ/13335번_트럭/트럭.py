#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13335                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207@gmail.com <boj.kr/u/lsw2207@gmail   +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13335                          #+#        #+#      #+#     #
#    Solved: 2025/10/28 10:22:17 by lsw2207@gmail.###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
- 문제:
    - 트럭의 개수, 다리 길이, 최대 하중
    - 트럭의 무게들.,,,,
    - 모든 트럭이 다리를 건너는 최단 시간
- 아이디어
    - 다리를 기준으로 다리의 길이를 고정. 0,0,으로 채움
    - 트럭이 하나 입장하면 앞의 0은 빠지고 뒤에 트럭이 들어옴. 
    - 만약 입장할 트럭이 없다면 앞의 0 빠지고 뒤에 0 추가...
    - 이런식으로 앞으; 0이 하나 빠질 때마다 시간을 증가시킴
'''
from collections import deque

N, W, L = map(int, input().split())
truck = deque(map(int, input().split()))

bridge = deque([0]*W)
time = 0
weight = 0

while bridge:
    time += 1
    weight -= bridge.popleft()

    if truck:
        if weight + truck[0] <= L:
            t = truck.popleft()
            bridge.append(t)
            weight += t

        else:
            bridge.append(0)
    
print(time)