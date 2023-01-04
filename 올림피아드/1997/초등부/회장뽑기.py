import sys;
input = sys.stdin.readline;
INF = int(1e9);

n = int(input());
Graph = [[INF] * (n + 1) for _ in range(n + 1)];
while True:
    a, b = map(int, input().split());
    if a == -1 and b == -1 :
        break;
    Graph[a][b] = 1;
    Graph[b][a] = 1;

for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if i == j :
            Graph[i][j] = 0;

for k in range(1, n + 1) :
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            Graph[i][j] = min(Graph[i][j], Graph[i][k] + Graph[k][j]);

scoreOfEachMember = [0] * (n + 1);
for i in range(1, n + 1) :
    maxDiff = 1;
    for diff in Graph[i][1 : ] :
        maxDiff = max(maxDiff, diff);
    scoreOfEachMember[i] = maxDiff;

scoreCriteria = min(scoreOfEachMember[1 : ]);
cntOfCandidate = scoreOfEachMember[1 : ].count(scoreCriteria);
candidateArr = [];
for idx in range(1, n + 1):
    if scoreOfEachMember[idx] == scoreCriteria :
        candidateArr.append(idx);

print(scoreCriteria, cntOfCandidate);
print(*candidateArr);