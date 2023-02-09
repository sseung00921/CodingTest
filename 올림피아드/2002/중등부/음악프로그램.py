import sys;
input = sys.stdin.readline;

n, m = map(int, input().split());
reqOrders = [];
Indegree = [0] * (n + 1);
Graph = [[] for _ in range(n + 1)];
Covered = [False] * (n + 1);
for _ in range(m) :
    req = list(map(int, input().split()));
    reqOrders.append(req[1 : ]);
for reqOrder in reqOrders :
    for i in range(0, len(reqOrder) - 1) :
        Graph[reqOrder[i]].append(reqOrder[i + 1]);
        Indegree[reqOrder[i + 1]] += 1;

answerList = [];
while len(answerList) < n :
    isCycle = True;
    for i in range(1, n + 1) :
        if Indegree[i] == 0 and not Covered[i] :
            isCycle = False;
            answerList.append(i);
            Covered[i] = True;
            for j in Graph[i] :
                Indegree[j] -= 1;
            break;
    if isCycle :
        answerList = [0];
        break;

for e in answerList :
    print(e);