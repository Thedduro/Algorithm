T = int(input())

for _ in range(T):
    left, right = [], []
    for s in input().rstrip():
        if s == '<':
            if left:
                right.append(left.pop())
        elif s == '>':
            if right:
                left.append(right.pop())
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)
    print(''.join(left+right[::-1])) # right은 현재 커서에서 가까운 순임.