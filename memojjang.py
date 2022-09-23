import sys
import heapq;

INF = int(1e9);
input = sys.stdin.readline;

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)];
d = [INF] * (v + 1);
d2 = [INF] * (v + 1);
d3 = [INF] * (v + 1);
for _ in range(e) :
    a, b, c = map(int, input().split());
    graph[a].append((c, b));
    graph[b].append((c, a));

mid1, mid2 = map(int, input().split());

d[1] = 0;
q = [(0, 1)];

while q :
    dist, now = heapq.heappop(q);
    if dist > d[now] :
        continue;
    for i in graph[now] :
        nDist = d[now] + i[0];
        if nDist < d[i[1]] :
            d[i[1]] = nDist;
            heapq.heappush(q, (nDist, i[1]));

d2[mid1] = 0;
q = [(0, mid1)];

while q :
    dist, now = heapq.heappop(q);
    if dist > d2[now] :
        continue;
    for i in graph[now] :
        nDist = d2[now] + i[0];
        if nDist < d2[i[1]] :
            d2[i[1]] = nDist;
            heapq.heappush(q, (nDist, i[1]));

d3[mid2] = 0;
q = [(0, mid2)];

while q :
    dist, now = heapq.heappop(q);
    if dist > d3[now] :
        continue;
    for i in graph[now] :
        nDist = d3[now] + i[0];
        if nDist < d3[i[1]] :
            d3[i[1]] = nDist;
            heapq.heappush(q, (nDist, i[1]));

hubo1 = d[mid1] + d2[mid2] + d3[v];
hubo2 = d[mid2] + d3[mid1] + d2[v];
answer = min(hubo1, hubo2);
if answer >= int(1e9) :
    answer = -1;
print(answer);