import sys;
input = sys.stdin.readline;

n = int(input());
info = [];
for _ in range(n) :
    sx, sy, w, h = map(float, input().split());
    sx = int(10*sx); sy = int(10*sy); w = int(10*w); h = int(10*h);
    ex = sx + w; ey = sy + h;
    info.append((sx, sy, ey, 1));
    info.append((ex, sy, ey, -1));

answer = 0;
info.sort();
hArr = [0] * 20002;
for i in range(len(info) - 1) :
    x, sy, ey, diff = info[i];
    if diff == 1 :
        for j in range(sy, ey) :
            hArr[j] += 1;
    elif diff == -1 :
        for j in range(sy, ey) :
            hArr[j] -= 1;
    w = info[i + 1][0] - info[i][0];
    h = 0;
    for j in range(20002) :
        if hArr[j] > 0 :
            h += 1;
    answer += (w*h);

if answer % 100 == 0 :
    print(int(answer / 100));
else :
    print(answer / 100.0);