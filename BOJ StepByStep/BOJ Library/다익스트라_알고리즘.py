import heapq;
INF = int(1e9);

v, e = map(int, input().split())
start = int(input());
graph = [[] for _ in range(v + 1)];
d = [INF] * (v + 1);
for _ in range(e) :
    a, b, c = map(int, input().split());
    graph[a].append((c, b));

d[start] = 0;
q = [(0, start)];

while q :
    dist, now = heapq.heappop(q);
    if dist > d[now] :
        continue;
    for i in graph[now] :
        nDist = d[now] + i[0];
        if nDist < d[i[1]] :
            d[i[1]] = nDist;
            heapq.heappush(q, (nDist, i[1]));

for i in range(1, v + 1) :
    if d[i] == INF :
        print("INF");
    else :
        print(d[i]);