import sys;
input = sys.stdin.readline;

n = int(input());
Graph = [[] for _ in range(n + 1)];
CalledCntForEachNode = [0] * (n + 1);
for _ in range(n) :
    parent, left, right = map(int, input().split());
    CalledCntForEachNode[parent] += 1;
    CalledCntForEachNode[left] += 1;
    CalledCntForEachNode[right] += 1;
    Graph[parent].append(left);
    Graph[parent].append(right);

nodesInEachLevel = [[] for _ in range(10011)];
def dfs(startNode, level, startCol) :
    summUnder = 0;
    leftNode = Graph[startNode][0];
    rightNode = Graph[startNode][1];

    leftStartCol = startCol
    if leftNode != -1 :
        summUnder += dfs(leftNode, level + 1, leftStartCol) + 1;
    rightStartCol = startCol + summUnder + 1;
    thisNodeCol = startCol + summUnder;
    if rightNode != -1 :
        summUnder += dfs(rightNode, level + 1, rightStartCol) + 1;

    nodesInEachLevel[level].append(thisNodeCol);

    return summUnder;

root = -1;
for i in range(1, n + 1) :
    if CalledCntForEachNode[i] == 1 :
        root = i;

dfs(root, 1, 1);

answerLevel = 1;
answerDist = 1;
for i in range(1, 10011) :
    if len(nodesInEachLevel[i]) < 2 :
        continue;
    mostLeft = min(nodesInEachLevel[i]);
    mosrRight = max(nodesInEachLevel[i]);
    thisDist = mosrRight - mostLeft + 1;
    if answerDist < thisDist :
        answerLevel = i;
        answerDist = thisDist;

print(answerLevel, answerDist);
