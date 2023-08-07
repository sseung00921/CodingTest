import sys;
input = sys.stdin.readline;
from collections import deque;

N, M, X = map(int, input().split());
GraphForBetter = [[] for _ in range(N + 1)];
GraphForWorse = [[] for _ in range(N + 1)];
for _ in range(M) :
    a, b = map(int, input().split());
    GraphForBetter[b].append(a);
    GraphForWorse[a].append(b);

Visited = [0] * (N + 1);
Visited[X] = 1;
q = deque([(0, X)]);
CntForBetter = -1;
while q :
    nowDepth, nowNode = q.popleft();
    for nextNode in GraphForBetter[nowNode] :
        if Visited[nextNode] == 1 :
            continue;
        Visited[nextNode] = 1;
        q.append((nowDepth + 1, nextNode));
CntForBetter = Visited.count(1) - 1;

Visited = [0] * (N + 1);
Visited[X] = 1;
q = deque([(0, X)]);
CntForWorse = -1;
while q :
    nowDepth, nowNode = q.popleft();
    for nextNode in GraphForWorse[nowNode] :
        if Visited[nextNode] == 1 :
            continue;
        Visited[nextNode] = 1;
        q.append((nowDepth + 1, nextNode));
CntForWorse = Visited.count(1) - 1;

print(CntForBetter + 1, N - CntForWorse);
