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

arr = deque(arr)
total_value = arr.popleft()
flag = False

while arr:
    operator = arr.popleft()
    num = arr.popleft()

    if operator == '-':
        flag = True
    
    if flag:
        total_value -= num
    
    else:
        total_value += num

print(total_value)