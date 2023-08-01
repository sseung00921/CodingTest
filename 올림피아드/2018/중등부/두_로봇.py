import sys;
input = sys.stdin.readline;
from collections import deque;

N, A, B = map(int, input().split());
Roads = [[] for _ in range(N + 1)];
for _ in range(N - 1) :
    src, dest, cost = map(int, input().split());
    Roads[src].append((cost, dest));
    Roads[dest].append((cost, src));

q = deque([(0, A)]);
Visited = [0] * (N + 1);
Visited[A] = 1;
Before = [(-1, -1)] * (N + 1);
Before[A] = (0, 0);
Answer = sys.maxsize;
while q :
    nowCost, nowNode = q.popleft();

    if nowNode == B :
        Answer = nowCost;
        break;

    for next in Roads[nowNode] :
        costBetween, nextNode = next;
        if not Visited[nextNode] :
            q.append((nowCost + costBetween, nextNode));
            Visited[nextNode] = 1;
            Before[nextNode] = (costBetween, nowNode);

MaxCost = Before[B][0];
nowPath = Before[B];
while True :
    costBetween, nowNode = nowPath;
    if nowNode == 0 :
        break;
    MaxCost = max(MaxCost, costBetween);
    nowPath = Before[nowNode];

print(Answer - MaxCost);