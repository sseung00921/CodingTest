import sys;
input = sys.stdin.readline;

t = int(input());
n = int(input());
a = list(map(int, input().split()));
m = int(input());
b = list(map(int, input().split()));

aD = [[0] * (n + 1) for _ in range(n + 1)];
bD = [[0] * (m + 1) for _ in range(m + 1)];
aM = dict();
bM = dict();
for i in range(n) :
    aD[i][i] = a[i];
    if aD[i][i] not in aM :
        aM[aD[i][i]] = 1;
    else :
        aM[aD[i][i]] += 1;
for i in range(m) :
    bD[i][i] = b[i];
    if bD[i][i] not in bM :
        bM[bD[i][i]] = 1;
    else :
        bM[bD[i][i]] += 1;
for i in range(0, n) :
    for j in range(i + 1, n) :
        aD[i][j] = aD[i][j - 1] + a[j];
        if aD[i][j] not in aM :
            aM[aD[i][j]] = 1;
        else :
            aM[aD[i][j]] += 1;
for i in range(0, m) :
    for j in range(i + 1, m) :
        bD[i][j] = bD[i][j - 1] + b[j];
        if bD[i][j] not in bM :
            bM[bD[i][j]] = 1;
        else :
            bM[bD[i][j]] += 1;

answer = 0;
for k in aM.keys() :
    if t - k in bM :
        answer += aM[k]*bM[t - k];
print(answer);