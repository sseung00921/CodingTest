import sys;
input = sys.stdin.readline;

N, M = map(int, input().split());
Memories = [None] + list(map(int, input().split()));
Costs = [0] + list(map(int, input().split()));

d = [[0] * (sum(Costs) + 1) for _ in range(N + 1)]
Answer = int(1e9);
for i in range(1, N + 1) :
    for j in range(0, sum(Costs) + 1) :
        if Costs[i] > j :
            d[i][j] = d[i - 1][j];
        else :
            d[i][j] = max(d[i - 1][j], d[i - 1][j - Costs[i]] + Memories[i]);

        if d[i][j] >= M :
            Answer = min(Answer, j);

print(Answer);
