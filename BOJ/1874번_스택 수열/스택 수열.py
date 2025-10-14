#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1874                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1874                           #+#        #+#      #+#     #
#    Solved: 2025/09/12 16:22:56 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    - 문제:
        - 1-N까지 순서대로 삽입하는데, pop을 정해진 수열 대로 해야함
        - push하면 +를 출력, pop을 하면 -를 출력함
        - N = 100,000
    - IDEA:
        - 스택에 마지막 원소가 나와 같다면을 기준으로 push와 pop을 수행
            - 현재 pop해야하는 숫자보다 커질때까지는 push 한다.
            - 그러다가 내가 나오면? > pop해서 수열을 만든다.
"""
def check():
    if stack[-1] == target:
        stack.pop()
        result = '-'
    else: # 마지막 원소가 지금 내가 아니야? 그럼 수열 만들기 불가.. > print('no')
        result = 'NO'
    return result

N = int(input())
arr = [int(input()) for _ in range(N)]

stack = []
n = 1

result = []
flag = True
for i in range(N):
    target = arr[i]

    while n <= target:
        stack.append(n)
        result.append('+')
        n += 1

    if check() == '-':
        result.append('-')
    else:
        flag = False
        print('NO')
        break

if flag == True:
    for v in result:
        print(v)