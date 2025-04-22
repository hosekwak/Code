n = int(input())
x, y = 1, 1
plans = input().split()

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]  # 위아래는 행 기준
dy = [-1, 1, 0, 0]  # 좌우는 열 기준

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n:
                x, y = nx, ny
            break  # 찾았으면 더 안 돌고 빠지기

print(x, y)
