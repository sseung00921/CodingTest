import heapq;
INF = int(1e9);

def dikestra(n, graph, src, dest, traps) :
    lenTraps = len(traps);
    q = [];
    visited = [[INF] * (1 << lenTraps) for _ in range(n + 1)];
    heapq.heappush(q, (0, src, 0));
    visited[src][0] = 0;
    while q :
        cost, nowNode, trapsBit = heapq.heappop(q);

        if cost > visited[nowNode][trapsBit] :
            continue;

        if nowNode == dest :
            return cost;

        nowTrapped = False;
        for i in range(lenTraps) :
            if nowNode == traps[i] :
                if trapsBit & (1 << i) != 0 :
                    nowTrapped = False;
                    trapsBit &= ~(1 << i);
                else :
                    nowTrapped = True;
                    trapsBit |= (1 << i);

        for v in range(1, n + 1) :
            if v == nowNode :
                continue;
            nextTrapped = False;
            for i in range(lenTraps) :
                if v == traps[i] :
                    if trapsBit & (1 << i) != 0 :
                        nextTrapped = True;
                    else :
                        nextTrapped = False;
            if nowTrapped == nextTrapped :
                nCost = cost + graph[nowNode][v]
            else :
                nCost = cost + graph[v][nowNode];
            if nCost < visited[v][trapsBit] :
                heapq.heappush(q, (nCost, v, trapsBit));
                visited[v][trapsBit] = nCost;
    return None;

def solution(n, start, end, roads, traps):
    graph = [[INF] * (n + 1) for _ in range(n + 1)];
    for i in range(1, n + 1) :
        graph[i][i] = 0;
    for road in roads :
        s, e, cost = road;
        if cost < graph[s][e] :
            graph[s][e] = cost;

    return dikestra(n, graph, start, end, traps);

n = 3;
start = 1;
end = 3;
roads = [[1, 2, 2], [3, 2, 3]];
traps = [2];
print(solution(n, start, end, roads, traps));

"""
또 다른 풀이
import heapq;

Graph = None;
INF = int(1e15);
Traps = None;
N = 0;
d = None;
def tuneGraphForThisTurn(trapsStatus) :
    for i in range((len(bin(trapsStatus)[2 : ]))) :
        if trapsStatus & (1 << i) > 0 :
            switchedNode = Traps[i];
            for j in range(1, N + 1) :
                if j == switchedNode :
                    continue;
                Graph[switchedNode][j], Graph[j][switchedNode] = Graph[j][switchedNode], Graph[switchedNode][j];
    return;

def solution(n, start, end, roads, traps):
    global Graph;
    global Traps;
    global N;
    global d;
    Graph = [[INF] * (n + 1) for _ in range(n + 1)];
    Traps = traps;
    N = n;
    for road in roads :
        frm, dest, cost = road;
        Graph[frm][dest] = min(cost, Graph[frm][dest]);
    d = [[INF] * (1 << len(traps) + 1) for _ in range(N + 1)];

    d[start][0] = 0;
    q = [(0, start, 0)];

    answer = 0;
    while q :
        dist, now, trapsStatus = heapq.heappop(q);
        if dist > d[now][trapsStatus] :
            continue;
        if now == end :
            answer = dist;
            break;
        tuneGraphForThisTurn(trapsStatus);
        for next in range(1, len(Graph[now])) :
            if now == next :
                continue;
            nDist = d[now][trapsStatus] + Graph[now][next];
            if next in Traps :
                idx = Traps.index(next);
                if trapsStatus & (1 << idx) > 0 :
                    nTrapStatus = trapsStatus & ~(1 << idx);
                else :
                    nTrapStatus = trapsStatus | (1 << idx);
            else :
                nTrapStatus = trapsStatus;
            if nDist < d[next][nTrapStatus] :
                d[next][nTrapStatus] = nDist;
                heapq.heappush(q, (nDist, next, nTrapStatus));
        tuneGraphForThisTurn(trapsStatus);
        
    return answer
"""