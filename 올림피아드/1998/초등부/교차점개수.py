import sys;

input = sys.stdin.readline;
N = int(input());
Points = [];
To = [0, 0, 2, 3, 1]
for _ in range(N//2) :
    a, b, c, d = map(int, input().split());
    if a == 2 or a == 3 :
        x = 50*To[a] + 50 - b;
    else :
        x = 50*To[a] + b;
    if c == 2 or c == 3 :
        y = 50*To[c] + 50 - d;
    else :
        y = 50*To[c] + d;


    Points.append((min(x, y), max(x, y)));

CheckCrossArr = [0] * (N//2);
for i in range(N//2) :
    for j in range(i + 1, N//2) :
        x1, y1 = Points[i];
        x2, y2 = Points[j];
        if x1 < x2 :
            if x2 < y1 and y1 < y2 :
                CheckCrossArr[i] += 1;
                CheckCrossArr[j] += 1;
        elif x1 > x2 :
            if x1 < y2 and y2 < y1 :
                CheckCrossArr[i] += 1;
                CheckCrossArr[j] += 1;

print(CheckCrossArr)
print(sum(CheckCrossArr)//2);
print(max(CheckCrossArr));
