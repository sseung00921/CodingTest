import sys;
input = sys.stdin.readline;

n = int(input());
data = [];
for i in range(n) :
    a, b = map(int, input().split());
    data.append((a, b));

Graph = [[] for _ in range(n)];
covered = [False] * n;
Indegree = [0] * n;

for i in range(n) :
    ai, bi = data[i];
    for j in range(n) :
        if i == j :
            continue;
        aj, bj = data[j];
        if min(aj, bj) <= min(ai, bi) and max(aj, bj) <= max(ai, bi) :
            Graph[i].append(j);
            Indegree[j] += 1;

maxStack = -1;
d = None;
def dfs(start) :
    global maxStack;

    if d[start] != -1 :
        return d[start];

    d[start] = 1;
    for next in Graph[start] :
        d[start] = max(d[start], 1 + dfs(next));

    maxStack = max(maxStack, d[start]);
    return d[start];

for i in range(n) :
    d = [-1] * n;
    dfs(i);

print(maxStack);