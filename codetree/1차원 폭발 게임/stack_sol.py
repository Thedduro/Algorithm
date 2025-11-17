'''
m = 2
94
94
94
52
52
52
94
인 경우, 원래는 52 3개외 94 3개가 동시에 터져서 94가 남아야 함.
근데 내 코드는 52 3개가 터지면 94 같은 클러스터로 묶여서 다 터짐
'''

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
numbers = numbers[::-1]

stack = []

for number in numbers:
    if stack and stack[-1][0] != number:
        if stack[-1][1] >= m:
            stack.pop()

    if stack and stack[-1][0] == number:
        val, cnt = stack[-1]
        stack[-1] = (val, cnt+1)

    if not stack or stack[-1][0] != number:
        stack.append((number, 1))

if stack[-1][1] >= m:
    stack.pop()

len = 0 
for v, c in stack:
    len += c
print(len)

while stack:
    num, cnt = stack.pop()
    for _ in range(cnt):
        print(num)