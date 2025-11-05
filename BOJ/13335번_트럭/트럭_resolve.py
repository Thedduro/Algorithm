from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)

weight = 0
time = 0

while trucks:
    time += 1
    weight -= bridge.popleft()

    if trucks[0]+weight <= L:
        truck = trucks.popleft()
        bridge.append(truck)
        weight += truck
    else:
        bridge.append(0)

print(time+w)

