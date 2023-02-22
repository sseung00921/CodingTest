import sys;
input = sys.stdin.readline;

n = int(input());
Graph = [[] for _ in range(n + 1)];
for _ in range(n) :
    parent, left, right = map(int, input().split());
    Graph[parent].append(left);
    Graph[parent].append(right);

def dfsLeft(start) :
    global LeftFromStartCnt;

    LeftFromStartCnt += 1;
    if Graph[start][0] == -1 :
        return;
    else :
        dfsLeft(Graph[start][0]);

def dfsRight(start) :
    global RightFromStartCnt;

    RightFromStartCnt += 1;
    if Graph[start][1] == -1 :
        return;
    else :
        dfsRight(Graph[start][1]);

LeftFromStartCnt = 0;
RightFromStartCnt = 0;
dfsLeft(1);
dfsRight(1);

MinStartMaxEndForEachLevelList = [[] for _ in range(20)];

for i in range(1, LeftFromStartCnt + 1) :
    MinStartMaxEndForEachLevelList[LeftFromStartCnt + 1 - i].append(i);

for i in range(1, RightFromStartCnt + 1) :
    MinStartMaxEndForEachLevelList[RightFromStartCnt + 1 - i].append(n + 1 - i);

answerLevel = -1;
answerDist = -1;
for i in range(len(MinStartMaxEndForEachLevelList)) :
    if len(MinStartMaxEndForEachLevelList[i]) < 2 :
        continue;
    if answerDist < MinStartMaxEndForEachLevelList[i][1] - MinStartMaxEndForEachLevelList[i][0] + 1 :
        answerLevel = i;
        answerDist = MinStartMaxEndForEachLevelList[i][1] - MinStartMaxEndForEachLevelList[i][0] + 1;
print(answerLevel, answerDist)