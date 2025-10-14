"""
    - 문제: 
        - 괄호를 쳐서 연산의 값이 최소가 되도록 한다.
        - 연산은 +, - 만 있다.
        - N = 250
    - IDEA:
        - '-'이 나오면 괄호 열고 ( 다음 '-'가 나올때까지 ')'를 닫는다
        - sub_sum을 만들어서 다음 '-'가 나올때까지 해당 부분의 더한다음 뺀다. 
"""

input_ = input().strip()
from collections import deque

result = 0

arr = []
temp = ''
for v in input_:
    if v in ['-', '+']: # +, - 이면 
        arr.append(int(temp))
        temp = ''
        arr.append(v)
    else: 
        temp += v
arr.append(int(temp))

result = 0
sub_sum = 0

arr = deque(arr)
while arr:
    current = arr.popleft()

    if current == '-': # -가 나오면
        flag = False

        while arr and not flag:
            next = arr[0]
            if next == '-': # -가 나오는 순간 
                result -= sub_sum
                sub_sum = 0
                flag =  True
            elif next != '+': #  숫자면
                sub_sum += arr.popleft()
            else: 
                arr.popleft()

    elif current != '+':
        result += current
    
    result -= sub_sum
print(result)