import sys;
input = sys.stdin.readline;
from collections import deque;

n = int(input());
d = [[0] * (n + 1) for _ in range(n + 1)];
m = int(input());
Indegree = [0] * (n + 1);
Graph = [[] for _ in range(n + 1)];
for _ in range(m) :
    a, b, c = map(int, input().split());
    Graph[b].append((a, c));
    Indegree[a] += 1;

q = deque([]);
for i in range(1, n + 1) :
    if Indegree[i] == 0 :
        q.append(i);

while q :
    now = q.popleft();
    if d[now].count(0) == n + 1 :
        d[now][now] = 1;

    for next, nextCnt in Graph[now] :
        for i in range(1, n + 1) :
            d[next][i] += d[now][i]*nextCnt;
        Indegree[next] -= 1;
        if Indegree[next] == 0 :
            q.append(next);

for i in range(1, n + 1) :
    if d[n][i] > 0 :
        print(i, d[n][i]);