import sys;
sys.setrecursionlimit(10**6);
input = sys.stdin.readline;
Length = 21;
n = int(input());
Graph = [[] for _ in range(n + 1)];
visited = [False] * (n + 1);
d = [-1] * (n + 1);
parent = [[0] * Length for _ in range(n + 1)];

def dfs(start, depth) :
    visited[start] = True;
    d[start] = depth;
    for node in Graph[start] :
        if visited[node] == False :
            parent[node][0] = start;
            dfs(node, depth + 1);

def setUp() :
    dfs(1, 0);
    for i in range(1, Length) :
        for j in range(1, n + 1) :
            parent[j][i] = parent[parent[j][i - 1]][i - 1];

def lcs(a, b) :
    if d[a] > d[b] :
        a, b = b, a;
    for i in range(Length - 1, -1, -1) :
        if d[b] - d[a] >= 2**i :
            b = parent[b][i];

    if a == b :
        return a;

    for i in range(Length - 1, -1, -1) :
        if parent[a][i] != parent[b][i] :
            a = parent[a][i];
            b = parent[b][i];

    return parent[a][0];


for _ in range(n - 1) :
    a, b = map(int, input().split());
    Graph[a].append(b);
    Graph[b].append(a);

setUp();
m = int(input());
for _ in range(m) :
    a, b = map(int, input().split());
    print(lcs(a, b));