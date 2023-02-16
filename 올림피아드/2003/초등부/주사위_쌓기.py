import sys;
input = sys.stdin.readline;
m = dict();
m[0] = 5; m[3] = 1;
m[1] = 3; m[4] = 2;
m[2] = 4; m[5] = 0;

n = int(input());
dices = [];
d = [[] * n for _ in range(6)];
for _ in range(n) :
    dices.append(list(map(int, input().split())));

for i in range(1, 7) :
    nowBottom = i;
    for j in range(n) :
        sideArr = [];
        bottomIdx = dices[j].index(nowBottom);
        topIdx = m[bottomIdx];
        nowTop = dices[j][topIdx]
        for k in range(6) :
            if k == bottomIdx or k == topIdx :
                continue;
            sideArr.append(dices[j][k]);
        d[i - 1].append(sideArr);
        nowBottom = nowTop;

maxVal = -1;
for i in range(6) :
    maxValInThisStart = 0;
    for j in d[i] :
        maxValInThisStart += max(j);
    maxVal = max(maxVal, maxValInThisStart);

print(maxVal)