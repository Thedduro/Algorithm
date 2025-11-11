n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
t = t % (n*2)
arr = u + d

for _ in range(t):
    temp = arr.pop()
    arr.insert(0, temp)

print(*arr[:n])
print(*arr[n:])