#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1406                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1406                           #+#        #+#      #+#     #
#    Solved: 2025/09/08 10:58:01 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    - 문제: 
        - N = 100,000, 명령횟수 M = 500,000
        - L: 왼쪽, D: 오른쪽, B: 왼쪽 문자 삭제, P$: $를 왼쪽에 추가
        - 명령어 수행 전 커서는 문장 맨뒤에 위치
    - IDEA:
        - 구현으로 풀어보자. 처음 커서의 시작은 마지막 맨뒤이다.
        > 이거 시간 초과 발생
"""
string = list(input())
M = int(input())
pointer = len(string) - 1

for i in range(M):
    m = str(input())

    if len(m) >= 2:
        s = m[2]
        string.insert(pointer + 1, s)
        pointer += 1
    else:
        if m == 'L' and pointer != -1:
            pointer -= 1
        elif m == 'D' and pointer != len(string) - 1:
            pointer += 1
        elif m == 'B' and pointer != -1 and string:
            string.pop(pointer)
            pointer -= 1

print(''.join(string))