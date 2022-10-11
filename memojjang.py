import sys;
input = sys.stdin.readline;
n, m = map(int,input().split());
memoryInfo = [0] + list(map(int, input().split()));
costInfo = [0] + list(map(int, input().split()));
SUM = sum(costInfo);
d = [[0] * (SUM + 1) for _ in range(n + 1)];

answer = int(1e9);
for i in range(1, n + 1) :
    byte = memoryInfo[i];
    cost = costInfo[i];
    for j in range(0, SUM + 1) :
        if cost > j :
            d[i][j] = d[i - 1][j];
        else :
            d[i][j] = max(byte + d[i - 1][j - cost], d[i - 1][j]);

        if d[i][j] >= m :
            answer = min(answer, j);

print(answer);
