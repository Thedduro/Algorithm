#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3273                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3273                           #+#        #+#      #+#     #
#    Solved: 2025/09/04 15:03:41 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    - 문제:
        - 더하면 자연수가 되는 수열의 쌍의 개수를 찾아라.
            - 모든 수는 다른수가 나옴
        - 수열 n = 1000000(십만) > n^2은 백억 = 터짐
        - 자연수 x = 2000000 > 자연수 x는 신경 안써도 됨.
    - idea:
        - 일단 각 수가 찾아야하는 쌍의 값을 구한다.
        - 원래 리스트에서 target이 있으면? cnt += 1  
"""

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

# target = list(map(lambda x: X - x, arr)) # n번의 연산 수행
cnt = 0

""" 이게 사실상 n^2연산이었음 > 시초
for i in range(N-1):
    if target[i] in arr[i+1:]:
        cnt += 1
"""
""" 그러면 그냥 while 문 돌면서 팝하고 > 있으면? 증가 
while arr:
    v = arr.pop()
    if X-v in arr: # 나와 쌍인 사람이 있음
        cnt += 1
> 이것도 사실상 n^2임 > fail
""" 
arr.sort() # NlogN
pointer = N-1

for i in range(N):
    target = X - arr[i]

    if i == pointer:
        break

    while arr[pointer] >= target:
        if target != arr[pointer]:
            pointer -= 1
        else:
            if i == pointer: 
                break
            cnt += 1
            pointer -= 1
            break

    if i >= pointer:
        break

print(cnt)