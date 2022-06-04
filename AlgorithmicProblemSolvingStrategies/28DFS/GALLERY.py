G = 0;
H = 0;
GRAPH = None;
VISITED = None;
UNWATCHED = 0;
INSTALLED = 1;
WATCHED = 2
INSTALLED_CNT = 0;

def dfs(here) :
    global INSTALLED_CNT;
    VISITED[here] = True;
    ChildrenStatus = [0, 0, 0];
    for there in GRAPH[here] :
        if VISITED[there] == False :
            ChildrenStatus[dfs(there)] += 1;

    if ChildrenStatus[UNWATCHED] > 0 :
        INSTALLED_CNT += 1;
        return INSTALLED;

    if ChildrenStatus[INSTALLED] > 0 :
        return WATCHED;

    return UNWATCHED;


tc = int(input());
while tc > 0 :
    INSTALLED_CNT = 0;
    G, H = map(int, input().split());
    GRAPH = [[] for _ in range(G)]
    VISITED = [False] * G;
    for _ in range(H) :
        a, b = map(int, input().split());
        GRAPH[a].append(b);
        GRAPH[b].append(a);

    for g in range(G) :
        if VISITED[g] == False :
            rtnStatus = dfs(g);
            if rtnStatus == UNWATCHED :
                INSTALLED_CNT += 1;
    print(INSTALLED_CNT);
    tc -= 1;