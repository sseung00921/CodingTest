import sys;
input = sys.stdin.readline;

n = int(input());

graph = [[0] * 102 for _ in range(102)];
d = [[0] * 102 for _ in range(102)];

for _ in range(n) :
    s, e = map(int, input().split());
    graph[s][e] = 1; graph[e][s] = 1;

for i in range(1, 101) :
    for j in range(i, 0, -1) :
        for k in range(j, i) :
            d[j][i] = max(d[j][i], d[j][k] + d[k][i] + graph[j][i]);

print(d[1][100]);
