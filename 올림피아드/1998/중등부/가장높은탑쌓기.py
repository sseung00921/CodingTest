import sys;
input = sys.stdin.readline;

n = int(input());
data = [];
numHeightMapper = dict();
d = [[None, -1] for _ in range(n + 1)];
for i in range(1, n + 1):
    area, h, weight = map(int, input().split());
    data.append((area, h, weight, i));
    numHeightMapper[i] = h;

Indegree = [0] * (n + 1);
covered = [False] * (n + 1);
Graph = [[] for _ in range(n + 1)];

for i in range(n):
    for j in range(i + 1, n):
        areai, hi, weighti, numi = data[i];
        areaj, hj, weightj, numj = data[j];
        if areai > areaj and weighti > weightj:
            Graph[numi].append(numj);
            Indegree[numj] += 1;
        elif areai < areaj and weighti < weightj:
            Graph[numj].append(numi);
            Indegree[numi] += 1;

def dfs(start):
    if d[start][1] != -1:
        return d[start][0], d[start][1];

    thisNode = [start];
    thisHeight = numHeightMapper[start];
    maxPath = [start];
    maxTotalHeight = numHeightMapper[start];
    for next in Graph[start]:
        subPath, subTotalHeight = dfs(next);
        if thisHeight + subTotalHeight > maxTotalHeight:
            maxPath = thisNode + subPath;
            maxTotalHeight = thisHeight + subTotalHeight;

    d[start][0] = maxPath;
    d[start][1] = maxTotalHeight;
    return d[start][0], d[start][1];


for i in range(1, n + 1):
    if Indegree[i] == 0:
        dfs(i);

maxTotalHeight = -1;
maxTotalHeightStartNum = -1;
for i in range(1, len(d)) :
    path, h = d[i];
    if h > maxTotalHeight :
        maxTotalHeight = h;
        maxTotalHeightStartNum = i;

print(len(d[maxTotalHeightStartNum][0]));
d[maxTotalHeightStartNum][0].reverse();
for block in d[maxTotalHeightStartNum][0]:
    print(block);
