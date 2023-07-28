import sys;
input = sys.stdin.readline;

N, K = map(int, input().split());
Info = [[0]];
for _ in range(N) :
    Info.append(list(map(int, input().split())));

INF = sys.maxsize;
d = [[-INF] * (K + 1) for _ in range(N + 1)];
d[0][0] = 0;
for i in range(1, N + 1) :
    for j in range(0, K + 1) :
        if d[i - 1][j] == -INF :
            continue;
        walkTime = Info[i][0]; walkReward = Info[i][1]; bikeTime = Info[i][2]; bikeReward = Info[i][3];
        if j + walkTime <= K :
            d[i][j + walkTime] = max(d[i][j + walkTime], d[i - 1][j] + walkReward);
        if j + bikeTime <= K :
            d[i][j + bikeTime] = max(d[i][j + bikeTime], d[i - 1][j] + bikeReward);

Answer = -1;
for i in range(0, K + 1) :
    Answer = max(Answer, d[N][i]);

print(Answer);
