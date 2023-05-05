from collections import deque;

N = 0;
Graph = None;
NodePutStatus = None;
Target = None;
ReachedCntForEachNode = None;
ReadyToDropNumList = None;
d = None;

def dropNum(num) :
    nowNode = 1;
    while len(Graph[nowNode]) != 0 :
        nextNode = Graph[nowNode][0];
        Graph[nowNode].append(Graph[nowNode].popleft());
        nowNode = nextNode;
    NodePutStatus[nowNode] += num;

    return nowNode;

def checkIfNodePutStatusIsGreagerThanTarget() :
    for i in range(1, N + 1) :
        if Target[i] > NodePutStatus[i] :
            return False;
    return True;

def getReachedCntForEachNode() :
    global ReachedCntForEachNode;
    ReachedCntForEachNode = [0] * (N + 1);
    while True :
        leafIdx = dropNum(3);
        ReachedCntForEachNode[leafIdx] += 1;
        if checkIfNodePutStatusIsGreagerThanTarget() :
            break;

def dfs(targetNum, targetCnt) :
    if d[targetNum][targetCnt] != -1 :
        return d[targetNum][targetCnt];

    if targetCnt == 0 :
        if targetNum == 0 :
            return [];
        else :
            return 0;

    rst = 0;
    for i in range(1, 4) :
        tmp = dfs(targetNum - i, targetCnt - 1)
        if tmp != 0 :
            if rst == 0 :
                rst = [i] + tmp;
            else :
                rst = min(rst, [i] + tmp);
    d[targetNum][targetCnt] = rst;
    return d[targetNum][targetCnt];

def getArrMakingNumWith123WhenGivenCnt(num, cnt) :
    return dfs(num, cnt);

def solution(edges, target):
    global N;
    global Graph;
    global NodePutStatus;
    global Target;
    global ReachedCntForEachNode;
    global ReadyToDropNumList;
    global d;
    N = len(edges) + 1;
    Graph = [[] for _ in range(N + 1)];
    NodePutStatus = [0] * (N + 1);
    Target = [0] + target;
    ReadyToDropNumList = [0] * (N + 1);
    d = [[-1] * 101 for _ in range(101)];
    for edge in edges :
        parent, child = edge;
        Graph[parent].append(child);
    for i in range(len(Graph)) :
        Graph[i].sort();
        Graph[i] = deque(Graph[i]);
    getReachedCntForEachNode();
    if max(ReachedCntForEachNode) > 100 :
        return [-1];
    for i in range(1, N + 1) :
        tmpArr = getArrMakingNumWith123WhenGivenCnt(Target[i], ReachedCntForEachNode[i]);
        if tmpArr == 0 :
            return [-1];
        ReadyToDropNumList[i] = deque(tmpArr);

    answer = [];
    NodePutStatus = [0] * (N + 1);
    Graph = [[] for _ in range(N + 1)];
    for edge in edges :
        parent, child = edge;
        Graph[parent].append(child);
    for i in range(len(Graph)) :
        Graph[i].sort();
        Graph[i] = deque(Graph[i]);
    while NodePutStatus != Target :
        leafIdx = dropNum(0);
        valueToSet = ReadyToDropNumList[leafIdx].popleft();
        NodePutStatus[leafIdx] += valueToSet;
        answer.append(valueToSet);
    return answer;

edges = [[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]];
target = [0, 0, 0, 3, 0, 0, 5, 1, 2, 3];
print(solution(edges, target));