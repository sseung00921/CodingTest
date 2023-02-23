import sys;
input = sys.stdin.readline;

n = int(input());
upData = list(map(int, input().split()));
downData = list(map(int, input().split()));
while 0 in upData :
    upData.remove(0);
while 0 in downData :
    downData.remove(0);
m1 = len(upData);
m2 = len(downData);
upData = [0] + upData;
downData = [0] + downData;

d = [[[0] * (m2 + 1) for _ in range(m1 + 1)] for _ in range(n + 1)];

for i in range(1, n + 1) :
    for j in range(1, min(m1 + 1, i + 1)) :
        for k in range(1, min(m2 + 1, i + 1)) :
            if j == i and k == i :
                d[i][j][k] = d[i - 1][j - 1][k - 1] + upData[j]*downData[k];
            elif j == i :
                d[i][j][k] = max(d[i - 1][j - 1][k], d[i - 1][j - 1][k - 1] + upData[j]*downData[k]);
            elif k == i :
                d[i][j][k] = max(d[i - 1][j][k - 1], d[i - 1][j - 1][k - 1] + upData[j]*downData[k]);
            else :
                d[i][j][k] = max(d[i - 1][j - 1][k], d[i - 1][j][k - 1], d[i - 1][j - 1][k - 1] + upData[j]*downData[k]);

print(d[n][m1][m2]);