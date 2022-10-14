import sys;
input = sys.stdin.readline;
INF = int(1e9);
n, m = map(int, input().split());

Graph = [[INF] * (n + 1) for _ in range(n + 1)];

for _ in range(m) :
    a, b, cost = map(int, sys.stdin.readline().split());
    Graph[a][b] = min(Graph[a][b], cost);

for k in range(1, n + 1) :
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            Graph[i][j] = min(Graph[i][j], Graph[i][k] + Graph[k][j]);

answer = INF;
for i in range(1, n + 1) :
    answer = min(answer, Graph[i][i]);

if answer < INF :
    print(answer);
else:
    print(-1);



