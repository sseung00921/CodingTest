N = 0;
D = 0;
P = 0;
T = 0;
Cache = None;
Lens = None;
Graph = None;

def dfs(townNum, days) :
    if days == 0 :
        return 1 if townNum == P else 0;

    if Cache[townNum][days] != -1 :
        return Cache[townNum][days];

    ret = 0;
    for linkedTownNum in range(N) :
        if Graph[townNum][linkedTownNum] == 0 :
            continue;
        ret += dfs(linkedTownNum, days - 1) * (1/Lens[linkedTownNum]);
    Cache[townNum][days] = ret;
    return Cache[townNum][days];



tc = int(input());
while tc > 0 :
    N, D, P = map(int, input().split());
    Graph = [[] for _ in range(N)]
    Lens = [0] * N;
    for i in range(N) :
        Graph[i] = list(map(int, input().split()));
        for j in range(N) :
            if Graph[i][j] == 1 :
                Lens[i] += 1;
    T = int(input());
    Q = list(map(int, input().split()));
    Cache = [[-1] * (D + 1) for _ in range(N + 1)];
    for searchedTownNum in Q :
        print(round(dfs(searchedTownNum, D), 8), end = ' ');
    tc -= 1;
