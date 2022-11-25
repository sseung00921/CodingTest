"""
아래는 1번이 Source이고 2번이 Sink일 때, 그리고 한번 지나간 노드는 다시는 지나지 않을 떄의 최대 유량을 구하는 알고리즘이다. 여기서 한번 지난 노드를 또 지나도 되도록
조건을 완화시켜주면 아래의 알고리즘에서 IN node와 OUT node를 각각 n개씩 분할해서 총 2n개의 노드에서 알고리즘을 사용하던 것을 그냥 n개의 노드로 단순히 입력 받고
그 n개의 노드간에서 직접적으로 방향 입력을 해주면 된다!.
"""

import sys;
input = sys.stdin.readline;
from collections import deque;

n, m = map(int, input().split());
out = n;
capacity = [[0] * (2*n + 2) for _ in range(2*n + 2)];
flow = [[0] * (2*n + 2) for _ in range(2*n + 2)];

for i in range(1, n + 1) :
    capacity[i][i + out] = 1; #노드 최대 허용 용량이 주어지는 경우는 노드 용량 c;
for _ in range(m) :
    a, b = map(int, input().split());
    capacity[a + out][b] = 1; #간선 최대 허용 용량이 주어지는 경우는 간선 용량 c;
    capacity[b + out][a] = 1; #간선 최대 허용 용량이 주어지는 경우는 간선 용량 c;


def bfs(source, sink, parents) :
    q = deque([source]);
    while q :
        start = q.popleft();
        for next in range(1, 2*n + 2) :
            if capacity[start][next] - flow[start][next] > 0 and parents[next] == -1 :
                parents[next] = start;
                q.append(next);
                if next == sink :
                    return True;
    return False;

def maxFlow(source, sink) :
    rtnVal = 0;
    while True :
        parents = [-1] * (2*n + 2);
        if not bfs(source, sink, parents) :
            return rtnVal;
        else :
            i = sink;
            tmp = int(1e11);
            while i != source :
                tmp = min(tmp, capacity[parents[i]][i] - flow[parents[i]][i]);
                i = parents[i];
            rtnVal += tmp;
            i = sink;
            while i != source :
                flow[parents[i]][i] += tmp;
                flow[i][parents[i]] -= tmp;
                i = parents[i];
    return rtnVal;

print(maxFlow(1 + out, 2));