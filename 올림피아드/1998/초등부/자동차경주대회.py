import sys;

input = sys.stdin.readline;
F = int(input());
N = int(input());
Dists = list(map(int, input().split()));
Costs = [0] + list(map(int, input().split())) + [0];

CumDists = [0] * len(Dists);
CumDists[0] = Dists[0];
for i in range(1, len(Dists)) :
    CumDists[i] = CumDists[i - 1] + Dists[i];

CumDists = [0] + CumDists;
TotalDist = CumDists[-1];

dCost = [-1] * (N + 1);
dCnt = [-1] * (N + 1);
dPath = [None] * (N + 1);

def dfs(nowNum) :
    if CumDists[nowNum] + F >= TotalDist :
        return 0, 0, [];
    if dCost[nowNum] != -1 :
        return dCost[nowNum], dCnt[nowNum], dPath[nowNum];
    tmp = sys.maxsize;
    for nextNum in range(nowNum + 1, N + 1) :
        if CumDists[nextNum] - CumDists[nowNum] <= F :
            if Costs[nextNum] + dfs(nextNum)[0] < tmp :
                tmp = Costs[nextNum] + dfs(nextNum)[0];
                dCost[nowNum] = Costs[nextNum] + dfs(nextNum)[0];
                dCnt[nowNum] = 1 + dfs(nextNum)[1];
                dPath[nowNum] = [nextNum] + dfs(nextNum)[2];
        else :
            break;
    return dCost[nowNum], dCnt[nowNum], dPath[nowNum];

print(dfs(0)[0]);
print(dfs(0)[1]);
print(*dfs(0)[2]);