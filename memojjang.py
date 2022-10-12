import sys;
import heapq;
input = sys.stdin.readline;
INF = int(1e9);

v = int(input());
e = int(input());
graph = [[] for _ in range(v + 1)];
d = [INF] * (v + 1);
prev = [-1] * (v + 1);
for _ in range(e) :
    a, b, c = map(int, input().split());
    graph[a].append((c, b));
start, end = map(int, input().split())
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
            prev[i[1]] = now;
            heapq.heappush(q, (nDist, i[1]));

print(d[end])
path = [end];
prevNode = prev[end];
while prevNode != -1 :
    path.append(prevNode);
    end = prevNode;
    prevNode = prev[end];
path.reverse();
print(len(path));
print(*path)