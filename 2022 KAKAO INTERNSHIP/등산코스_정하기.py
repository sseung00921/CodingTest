import heapq;
Graph = None;
INF = int(1e9);

def solution(n, paths, gates, summits):
    global Graph;
    Graph = [[] for _ in range(n + 1)];
    for path in paths :
        a, b, cost = path;
        Graph[a].append((b, cost));
        Graph[b].append((a, cost));
    summits = set(summits);
    q = [];
    intenForEachNode = [INF] * (n + 1);
    for gate in gates :
        heapq.heappush(q, (0, gate));
        intenForEachNode[gate] = 0;

    minIndensity = INF;
    minSummitArr = [];
    while q :
        nowNodeInten, nowNodeNum = heapq.heappop(q);

        if nowNodeInten > minIndensity :
            break;

        if nowNodeNum in summits :
            minIndensity = nowNodeInten;
            minSummitArr.append(nowNodeNum);
            continue;

        if nowNodeInten > intenForEachNode[nowNodeNum] :
            continue;

        for nextNode in Graph[nowNodeNum] :
            nextNodeNum = nextNode[0];
            nextNodeInten = max(nowNodeInten, nextNode[1]);
            if nextNodeInten < intenForEachNode[nextNodeNum] :
                heapq.heappush(q, (nextNodeInten, nextNodeNum));
                intenForEachNode[nextNodeNum] = nextNodeInten;

    minSummitArr.sort();
    minSummit = minSummitArr[0];
    return [minSummit, minIndensity];

n = 6;
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]];
gates = [1, 3];
summits = [5];
print(solution(n, paths, gates, summits));