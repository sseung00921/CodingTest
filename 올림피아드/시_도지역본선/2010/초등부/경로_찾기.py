import sys;
input = sys.stdin.readline;
import heapq;

N, K = map(int, input().split());
arr = [None];
for _ in range(N) :
    arr.append(input().rstrip());

Start, End = map(int, input().split());

Graph = [[] for _ in range(N + 1)];

def isHaeming(i, j) :
    strA = arr[i];
    strB = arr[j];
    cnt = 0;
    for idx in range(K) :
        if strA[idx] != strB[idx] :
            cnt += 1;
        if cnt > 1 :
            return False;
    return cnt == 1;

for i in range(1, N + 1) :
    for j in range(i + 1, N + 1) :
        if isHaeming(i, j) :
            Graph[i].append(j);
            Graph[j].append(i);

INF = int(1e9);
d = [INF] * (N + 1);
d[Start] = 0;
q = [(0, Start)];
Parents = [-1] * (N + 1);
while q :
    nowDist, nowNode = heapq.heappop(q);
    if nowNode == End :
        break;
    if nowDist > d[nowNode] :
        continue;

    for nextNode in Graph[nowNode] :
        nextDist = nowDist + 1;
        if nextDist < d[nextNode] :
            d[nextNode] = nextDist;
            Parents[nextNode] = nowNode;
            heapq.heappush(q, (nextDist, nextNode));

if d[End] == INF :
    print(-1);
else :
    Path = [End];
    NowNode = End;
    while Parents[NowNode] != -1 :
        Path.append(Parents[NowNode]);
        NowNode = Parents[NowNode];
    Path.reverse();
    print(*Path);
