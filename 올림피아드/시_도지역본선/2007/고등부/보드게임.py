import sys;
input = sys.stdin.readline;

N = int(input());
data = list(input().split());
M, K = map(int, input().split());
Graph = [[] for _ in range(M + 1)];
for _ in range(K) :
    a, b, val = input().split();
    a = int(a); b = int(b);
    Graph[a].append((b, val));
    Graph[b].append((a, val));

d = [[-1] * (M + 1) for _ in range(N + 1)];

def dfs(nowTurn, nowCity) :
    if d[nowTurn][nowCity] != -1 :
        return d[nowTurn][nowCity];

    if nowTurn == N :
        return 0;

    temp = 0;
    for nextCityAndRoad in Graph[nowCity] :
        nextCity, nextRoad = nextCityAndRoad;
        if nextRoad == data[nowTurn] :
            temp = max(temp, dfs(nowTurn + 1, nextCity) + 10);
        else :
            temp = max(temp, dfs(nowTurn + 1, nextCity));

    d[nowTurn][nowCity] = temp;
    return d[nowTurn][nowCity];

print(dfs(0, 1));