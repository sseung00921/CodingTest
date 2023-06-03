import sys;
input = sys.stdin.readline;

n = int(input());
arr = [-1] * 501;
maxA = -1;
for _ in range(n) :
    a, b = map(int, input().split());
    maxA = max(maxA, a)
    arr[a] = b;
d = [[0] * 2 for _ in range(maxA + 1)];

def cntUnCrossMaxCnt(aIdx) :
    rtnVal = 0;
    bPos = arr[aIdx];
    for i in range(aIdx - 1, 0, -1) :
        if arr[i] == -1 :
            continue;
        if arr[i] > bPos :
            continue;
        rtnVal = max(rtnVal, d[i][1]);
    return rtnVal;

d[1][0] = 0;
d[1][1] = 1 if arr[1] != -1 else 0;
for i in range(2, maxA + 1) :
    if arr[i] == -1 :
        d[i][0] = max(d[i - 1][0], d[i - 1][1]);
        d[i][1] = 0;
    elif arr[i] != -1 :
        d[i][0] = max(d[i - 1][0], d[i - 1][1]);
        d[i][1] = cntUnCrossMaxCnt(i) + 1;

print(n - max(d[maxA][0], d[maxA][1]));
