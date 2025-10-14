#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5397                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5397                           #+#        #+#      #+#     #
#    Solved: 2025/09/09 11:47:39 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
    - 문제:
        - 비밀번호를 알아낸다.
        - 백스페이스(-), 화살표(<,>)를 감지해라
        - N = 1,000,000
    - IDEA:
        - 비밀번호 리스트에 추가하고, 지운다
        - 커서의 위치는 어떻게 구현할까?
            - >, < 나오면 비밀번호 인덱스를 조정하고
            - 백스페이스, 문자가 나오면 그 위치에서 추가, 빼기
            - pop(index)등을 쓰면 시초 > 그 위치까지 쪼갠다음 두 리스트를 더하자
"""

T = int(input())

for _ in range(T):
    string = list(input())
    password = []
    pointer = len(password)-1

    for s in string:
        if s == '<':
            pointer -= 1
            if pointer < 0:
                pointer = 0
        elif s == '>':
            pointer += 1
            if pointer >= len(password)-1:
                pointer = len(password)-1
        elif s == '-':
            password = password[:pointer] + password[pointer+1:]
        elif s: 
            password = password[:pointer]+ [s] + password[pointer:]
            pointer += 1
        print(pointer, password)
    print(''.join(password))