import sys;
sys.setrecursionlimit(100000);

INF = 1000000
PI = None;
Len = 0;
Cache = None;

def score(start, end) :
    repeative = True;
    for i in range(start, end - 1) :
        if PI[i + 1] != PI[i] :
            repeative = False;
            break;
    if repeative :
        return 1;
    progressive = True;
    for i in range(start, end - 1) :
        if PI[i + 1] - PI[i] != PI[start + 1] - PI[start] :
            progressive = False;
            break;
    if progressive and abs(PI[start + 1] - PI[start]) == 1 :
        return 2;
    alternating = True;
    for i in range(start, end) :
        if i + 2 < end and PI[i + 2] != PI[i] :
            alternating = False;
            break;
    if alternating :
        return 4;
    if progressive :
        return 5;
    return 10;

def dfs(idx) :
    if idx == Len :
        return 0;
    if Cache[idx] != INF :
        return Cache[idx];
    for off in range(3, 6) :
        if idx + off <= Len :
            Cache[idx] = min(Cache[idx], score(idx, idx + off) + dfs(idx + off));
    return Cache[idx];

tc = int(input());
while tc > 0 :
    pi = input();
    Len = len(pi);
    Cache = [INF] * Len;
    PI = [INF] * Len;
    for i in range(Len) :
        PI[i] = int(pi[i]);
    print(dfs(0));
    tc -= 1;
