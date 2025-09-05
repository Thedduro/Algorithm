#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13300                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13300                          #+#        #+#      #+#     #
#    Solved: 2025/09/05 14:57:14 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    - 각 학년 별 / 성별 방을 배정한다.
    - N = 학생 수, K = 한 방의 최대 인원 수

    - idea:
        - 각 학년 세그멘트별로 K로 나눠 -> n+1//K
        그 값을 다 더해  
"""

N, K = map(int, input().split())
dict = {i: [0, 0] for i in range(1,7)}
for _ in range(N):
    sex, year = map(int, input().split())
    if sex == 0:
        dict[year][0] += 1
    else:
        dict[year][1] += 1

cnt = 0 # 방 개수

def find(x):
    global cnt
    
    v = x // K
    cnt += v
    if x % K != 0:
        cnt += 1 

for x, y in dict.values():
    # 나누고, 몫이 =0이 아니면 + 1 을 더해줌
    find(x)
    find(y)

print(cnt)