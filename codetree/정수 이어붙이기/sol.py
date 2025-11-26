n, k = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

result = set()
visited = [False] * n

# Please write your code here.
def dfs(number, cnt):
    if cnt == k:
        result.add(number)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(number+str(numbers[i]), cnt+1)
            visited[i] = False


dfs('',0)
print(result)