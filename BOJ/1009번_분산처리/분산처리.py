#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1009                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1009                           #+#        #+#      #+#     #
#    Solved: 2025/08/02 19:23:34 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    # 거듭제곱은 패턴을 이룬다 > 마지막 자릿수는 패턴을 이룬다
    a %= 10
    if a == 0:
        print(10)
        continue
    pattern = []
    temp_num = a
    
    while temp_num not in pattern:
        pattern.append(temp_num)
        temp_num = (temp_num * a) % 10

    index = (b - 1) % len(pattern)
    print(pattern[index])