x1, y1, r1 = [int(i) for i in input().split()]
x2, y2, r2 = [int(i) for i in input().split()]
if (x1 - x2) ** 2 + (y1 - y2) ** 2 > (r1 + r2) ** 2:
    print('NO')
else:
    print('YES')
