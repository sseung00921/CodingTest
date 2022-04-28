from collections import deque;

n, m = map(int, input().split());
parents = [0] * (n + 1);
for i in range(1, n + 1) :
    parents[i] = i;

def findParent(parents, x) :
    if parents[x] != x :
        parents[x] = findParent(parents, parents[x]);
    return parents[x];

def unionParent(parents, a, b) :
    a = findParent(parents, a);
    b = findParent(parents, b);
    if a < b :
        parents[b] = parents[a];
    else :
        parents[a] = parents[b];

roads = [];
for _ in range(m) :
    a, b, cost = map(int, input().split());
    roads.append((cost, a, b));

roads.sort();

totalCost = 0;
maxCost = 0;
q = deque(roads);
while q :
    cost, a, b = q.popleft();
    if findParent(parents, a) == findParent(parents, b) :
        continue;
    else :
        unionParent(parents, a, b);
        totalCost += cost;
        maxCost = max(maxCost, cost);

print(totalCost - maxCost);
