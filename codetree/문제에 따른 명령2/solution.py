dirs = input()

direction = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
next_direction = {
    'U': {'L': 'L', 'R': 'R'},
    'R': {'L': 'U', 'R': 'D'},
    'D': {'L': 'R', 'R': 'L'},
    'L': {'L': 'D', 'R': 'U'}
}

x, y = 0, 0
command = 'U'

for d in dirs:
    if d in ['L', 'R']:
        command = next_direction[command][d]

    if d == 'F': # 명령일때, 지금 command를 direction에서 찾아서 실행
        dx, dy = direction[command]
        x, y = dx+x, dy+y

print(x, y)
