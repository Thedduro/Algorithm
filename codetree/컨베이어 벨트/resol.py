from collections import deque

n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

arr = u+d[::-1]
arr = deque(arr[::-1])

t = t % (n*2)

for _ in range(t):
    num = arr.popleft()
    arr.append(num)

arr = list(arr[::-1])
print(*arr[:n])
print(*arr[n:])
