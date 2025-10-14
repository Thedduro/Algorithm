#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10828                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10828                          #+#        #+#      #+#     #
#    Solved: 2025/09/10 13:25:09 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
    - 문제:
        - 스택을 구현해라.
        - N = 10,000
"""

N = int(input())
stack = []

for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else: # 스택이 비어있으면
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    else: # top
        if stack:
            print(stack[-1])
        else: # 스택이 비어있으면
            print(-1)