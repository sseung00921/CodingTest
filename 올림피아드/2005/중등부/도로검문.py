import sys;
input = sys.stdin.readline;
import heapq;

n, m = map(int, input().split());
Graph = [[] for _ in range(n + 1)];
for _ in range(m) :
    a, b, t = map(int, input().split());
    Graph[a].append((b, t));
    Graph[b].append((a, t));

INF = int(1e9);
d = [INF] * (n + 1);
prev = [-1] * (n + 1);
d[1] = 0;
q = [(0, 1)];

def dijkStra(checkPointA, checkPointB) :
    while q :
        dist, now = heapq.heappop(q);
        if dist > d[now] :
            continue;
        for i in Graph[now] :
            if now == checkPointA and i[0] == checkPointB or now == checkPointB and i[0] == checkPointA :
                nDist = d[now] + INF;
            else :
                nDist = d[now] + i[1];
            if nDist < d[i[0]] :
                d[i[0]] = nDist;
                prev[i[0]] = now;
                heapq.heappush(q, (nDist, i[0]));

dijkStra(-1, -1);
bestWithoutCheck = d[n];

path = [n];
prevNode = prev[n];
while prevNode != -1 :
    path.append(prevNode);
    end = prevNode;
    prevNode = prev[end];
path.reverse();

answer = -1;
d = [INF] * (n + 1);
d[1] = 0;
q = [(0, 1)];
for i in range(0, len(path) - 1) :
    checkPointA = path[i];
    checkPointB = path[i + 1];
    dijkStra(checkPointA, checkPointB);
    answer = max(answer, d[n] - bestWithoutCheck)
    d = [INF] * (n + 1);
    d[1] = 0;
    q = [(0, 1)];

if answer > 20000000 :
    answer = -1;
print(answer);