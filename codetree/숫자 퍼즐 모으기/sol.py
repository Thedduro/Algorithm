N, M = map(int, input().split())
puzzles = [list(map(int, input().split())) for _ in range(N)]

minimum = N

def recursive(idx, numbers, cnt):
    global minimum

    if cnt >= minimum:
        return

    if len(numbers) == 10:
        minimum = min(minimum, cnt)
        return

    for i in range(idx, N):
        new_numbers = numbers | set(puzzles[i])
        recursive(idx+1, new_numbers, cnt+1)

recursive(0,set(),0)

print(minimum)
