INF = -int(1e9);
N = 0; M = 0;
A = None; B = None;
Cache = None;

def dfs(aIdx, bIdx) :
    if Cache[aIdx + 1][bIdx + 1] != -1 :
        return Cache[aIdx + 1][bIdx + 1];

    Cache[aIdx + 1][bIdx + 1] = 2;
    aElement = -1 if aIdx == INF else A[aIdx];
    bElement = -1 if bIdx == INF else B[bIdx];
    maxElement = max(aElement, bElement);

    for aNext in range(aIdx + 1, N) :
        if maxElement < A[aNext] :
            Cache[aIdx + 1][bIdx + 1] = max(Cache[aIdx + 1][bIdx + 1], dfs(aNext, bIdx) + 1);
    for bNext in range(bIdx + 1, M) :
        if maxElement < B[bNext] :
            Cache[aIdx + 1][bIdx + 1] = max(Cache[aIdx + 1][bIdx + 1], dfs(aIdx, bNext) + 1);

    return Cache[aIdx][bIdx];


tc = int(input());
while tc > 0 :
    Cache = [[-1] * 102 for _ in range(102)];
    N, M = map(int, input().split());
    A = list(map(int, input().split()));
    B = list(map(int, input().split()));
    print(dfs(-1,-1) - 2)
    print(Cache);
    tc -= 1;