import sys;
sys.setrecursionlimit(10 ** 4);

Parents = None;
NodeKinds = None;
Graph = None;
N = 0;

def find_parent(x):
    if Parents[x] != x:
        Parents[x] = find_parent(Parents[x])
    return Parents[x]

def union_parent(a, b):
    oa, ob = a, b;
    a = find_parent(a)
    b = find_parent(b)
    if NodeKinds[oa] == 0 and NodeKinds[a] > 0 and NodeKinds[a] == NodeKinds[b] :
        if b < a :
            isVisited = [0] * (N + 1);
            setParents(oa, b, isVisited);
    elif NodeKinds[ob] == 0 and NodeKinds[b] > 0 and NodeKinds[b] == NodeKinds[a] :
        if a < b :
            isVisited = [0] * (N + 1);
            setParents(ob, a, isVisited);
    elif NodeKinds[a] == 0 and NodeKinds[b] == 0 :
        if a < b:
            Parents[b] = a
        else:
            Parents[a] = b
    elif NodeKinds[a] == 0 and NodeKinds[b] > 0 :
        Parents[a] = b;
    elif NodeKinds[b] == 0 and NodeKinds[a] > 0 :
        Parents[b] = a;

def setParents(start, parent, isVisited) :
    isVisited[start] = 1;
    Parents[start] = parent;
    for next in Graph[start] :
        if NodeKinds[next] != 0 :
            continue;
        if isVisited[next] :
            continue;
        setParents(next, parent, isVisited);

def solution(n, paths, gates, summits):
    global NodeKinds;
    global Parents;
    global Graph;
    global N;
    N = n;
    NodeKinds = [0] * (n + 1); #1은 출입구 2는 산봉우리
    for gate in gates :
        NodeKinds[gate] = 1;
    for summit in summits :
        NodeKinds[summit] = 2;

    Parents = [0] + [i for i in range(1, n + 1)];
    paths.sort(key = lambda x : x[2]);

    Graph = [[] for _ in range(n + 1)];

    minCost = -1;
    minSubmitNum = -1;
    for path in paths :
        a, b, cost = path;
        Graph[a].append(b);
        Graph[b].append(a);
        if minCost != -1 and cost > minCost :
            break;
        parentAKind = NodeKinds[find_parent(a)];
        parentBKind = NodeKinds[find_parent(b)];
        if parentAKind == 1 and parentBKind == 2 or parentAKind == 2 and parentBKind == 1 :
            minCost = cost;
            if parentAKind == 2 :
                minSubmitNum = find_parent(a) if minSubmitNum == -1 else min(minSubmitNum, find_parent(a));
            elif parentBKind == 2 :
                minSubmitNum = find_parent(b) if minSubmitNum == -1 else min(minSubmitNum, find_parent(b));
        else:
            union_parent(a, b);
    answer = [minSubmitNum, minCost]
    return answer

n = 6;
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]];
gates = [1, 3];
summits = [5];
print(solution(n, paths, gates, summits));

n = 5;
paths = [[4, 2, 1], [2, 3, 1], [1, 3, 2], [3, 5, 3]];
gates = [5];
summits = [1, 4];
print(solution(n, paths, gates, summits));