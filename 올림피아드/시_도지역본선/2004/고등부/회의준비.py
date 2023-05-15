import sys;
input = sys.stdin.readline;
import heapq;

def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if Parents[x] != x:
        Parents[x] = find_parent(Parents[x])
    return Parents[x]

# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        Parents[b] = a
    else:
        Parents[a] = b

def findRep(parentIdx) :
    minMaxDist = int(1e9);
    rtnVal = -1;
    for e in Groups[parentIdx] :
        dist = calDistWhenParamIsRep(parentIdx, e)
        if dist < minMaxDist :
            minMaxDist = dist;
            rtnVal = e;
    if rtnVal == -1 :
        rtnVal = parentIdx;
    return rtnVal;

def calDistWhenParamIsRep(parentIdx, e) :
    group = Groups[parentIdx];
    maxx = -1;
    for i in group :
        if i == e :
            continue;
        maxx = max(maxx, calDistBetweenTwo(parentIdx, i, e));
    return maxx;

def calDistBetweenTwo(parentIdx, start, end) :
    d = [int(1e9)] * (n + 1);
    d[start] = 0;
    q = [(0, start)];
    graph = Graphs[parentIdx];

    while q :
        dist, now = heapq.heappop(q);

        if dist > d[now] :
            continue;

        for i in graph[now] :
            nDist = d[now] + 1;
            if nDist < d[i] :
                d[i] = nDist;
                heapq.heappush(q, (nDist, i));

    return d[end];

n = int(input());
m = int(input());
Parents = [i for i in range(0, n + 1)];
RelationShips = [];
for _ in range(m) :
    a, b = map(int, input().split());
    RelationShips.append((a, b));
    union_parent(a, b);

for i in range(1, len(Parents)) :
    Parents[i] = find_parent(i);

Graphs = [[[] for _ in range(n + 1)] for _ in range(n + 1)];
Groups = [set() for _ in range(n + 1)];
keySet = set(Parents[1 : ]);
for relationShip in RelationShips :
    a, b = relationShip;
    graph = Graphs[find_parent(a)];
    graph[a].append(b);
    graph[b].append(a);
    group = Groups[find_parent(a)];
    group.add(a);
    group.add(b);

Answers = [];
for i in range(1, n + 1) :
    if i in keySet :
        Answers.append(findRep(i));

print(len(Answers));
Answers.sort();
for e in Answers :
    print(e);