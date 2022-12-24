x1, y1, w1, h1 = [int(i) for i in input().split()]
x2, y2, w2, h2 = [int(i) for i in input().split()]
if ((x2 <= x1 + w1 <= x2 + w2 or x2 <= x1 <= x2 + w2)
        or (y2 <= y1 + h1 <= y2 + h2 or y2 <= y1 <= y2 + h2)):
    print('YES')
else:
    print('NO')