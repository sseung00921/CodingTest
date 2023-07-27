import sys;
input = sys.stdin.readline;

N, M = map(int, input().split());
CanNotGo = set(list(map(int, input().split())));
INF = sys.maxsize;
d = [[INF] * 51 for _ in range(N + 5)];
d[0][0] = 0;
for i in range(1, N + 1) :
    for j in range(0, 49) :
        if d[i - 1][j] == INF :
            continue;
        if i in CanNotGo :
            d[i][j] = min(d[i][j], d[i - 1][j]);
        elif i not in CanNotGo :
            if j >= 3 :
                d[i][j - 3] = min(d[i][j - 3], d[i - 1][j]);
            d[i][j] = min(d[i][j], d[i - 1][j] + 10000);
        for k in range(0, 3) :
            d[i + k][j + 1] = min(d[i + k][j + 1], d[i - 1][j] + 25000);
        for k in range(0, 5) :
            d[i + k][j + 2] = min(d[i + k][j + 2], d[i - 1][j] + 37000);

print(min(d[N]));
