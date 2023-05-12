import sys;
from collections import deque;
input = sys.stdin.readline;

N = int(input());
M = int(input());
Graph = [[] for _ in range(N + 1)];
for _ in range(M) :
    a, b = map(int, input().split());
    Graph[a].append(b);
    Graph[b].append(a);

IsVisited = [0] * (N + 1);
IsVisited[1] = 1;
q = deque([1]);

while q :
    nowNode = q.popleft();

    for nextNode in Graph[nowNode] :
        if IsVisited[nextNode] == 1 :
            continue;
        IsVisited[nextNode] = 1;
        q.append(nextNode);

print(IsVisited.count(1) - 1);