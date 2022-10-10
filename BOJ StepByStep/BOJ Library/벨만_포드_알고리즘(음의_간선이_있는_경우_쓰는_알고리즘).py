import sys;
input = sys.stdin.readline;

INF = int(1e9);
n, m = map(int, input().split());
edges = [];
d = [INF] * n;
for _ in range(m) :
    a, b, cost = map(int, input().split());
    edges.append((a - 1, b - 1, cost));

def bf(start) :
    d[start] = 0;
    for i in range(n) :
        for edge in edges :
            src = edge[0];
            dest = edge[1];
            cost = edge[2];
            if d[src] != INF and d[dest] > d[src] + cost :
                d[dest] = d[src] + cost;
                if i == n - 1 :
                    return False;
    return True;

if not bf(0) :
    print(-1);
else :
    for i in range(1, len(d)) :
        if d[i] == INF :
            print(-1);
        else :
            print(d[i]);
