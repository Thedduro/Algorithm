string = list(input())
M = int(input())

"""
    - IDEA:
        - 키로거 문제의 풀이처럼
        - 현재의 커서를 기준으로 left와 right 리스트로 나눈다
        - L: left를 right에 옮김
        - R: right를 left에 옮김
        - B: left의 마지막 요소를 삭제함
        - P: 등장 문자열을 left에 삽입함
"""

left, right = list(input()), []
M = int(input())

for _ in range(M):
    command = input().split()

    if command[0] == 'L':
        if left: # 맨 앞이 아니라면
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(command[1])
    
print(''.join(left + right[::-1]))
