import sys;
INF = int(1e9);
n = int(sys.stdin.readline());
m = int(sys.stdin.readline());

Graph = [[INF] * (n + 1) for _ in range(n + 1)];

for _ in range(m) :
    a, b, cost = map(int, sys.stdin.readline().split());
    Graph[a][b] = min(Graph[a][b], cost);

for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if i == j :
            Graph[i][j] = 0;

for k in range(1, n + 1) :
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            Graph[i][j] = min(Graph[i][j], Graph[i][k] + Graph[k][j]);

for i in range(1, n + 1) :
    print(*Graph[i][1 : ]);