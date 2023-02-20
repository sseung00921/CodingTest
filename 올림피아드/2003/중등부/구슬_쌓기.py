n, m = map(int, input().split());
GraphHeavy = [[] for _ in range(n + 1)];
GraphLight = [[] for _ in range(n + 1)];
for _ in range(m) :
    heavy, light = map(int, input().split());
    GraphHeavy[light].append(heavy);
    GraphLight[heavy].append(light);

Cnt = 0;
IsVisited = [False] * (n + 1);
def dfs(start, Graph) :
    global Cnt;
    IsVisited[start] = True;
    for next in Graph[start] :
        if not IsVisited[next] :
            Cnt += 1;
            dfs(next, Graph);
    return;

MiddleIdx = (n + 1) // 2;

answerCnt = 0;
for i in range(1, n + 1) :
    Cnt = 0;
    IsVisited = [False] * (n + 1);
    dfs(i, GraphHeavy);
    if Cnt >= MiddleIdx :
        answerCnt += 1;
        continue;
    Cnt = 0;
    IsVisited = [False] * (n + 1);
    dfs(i, GraphLight);
    if Cnt >= MiddleIdx :
        answerCnt += 1;

print(answerCnt);