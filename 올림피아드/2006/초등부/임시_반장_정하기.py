import sys;
input = sys.stdin.readline;

n = int(input());
data = [];
for _ in range(n) :
    data.append(list(map(int, input().split())));

d = [[0] * n for _ in range(n)];

for i in range(len(data)) :
    for j in range(i + 1, len(data)) :
        for k in range(5) :
            if data[i][k] == data[j][k] :
                d[i][j] = 1;
                d[j][i] = 1;
                break;

answer = -1;
maxCommonCnt = -1;
for i in range(len(d)) :
    commonCnt = d[i].count(1);
    if commonCnt > maxCommonCnt :
        answer = i + 1;
        maxCommonCnt = commonCnt;

print(answer);