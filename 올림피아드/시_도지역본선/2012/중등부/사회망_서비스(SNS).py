import sys;
input = sys.stdin.readline;
sys.setrecursionlimit(10**6 + 10);

N = int(input());
Graph = [[] for _ in range(N + 1)];
for _ in range(N - 1) :
    a, b = map(int, input().split());
    Graph[a].append(b);
    Graph[b].append(a);

d = [[-1]*2 for _ in range(N + 1)];
IsVisited = [0] * (N + 1);
def dfs(now, isEarlier) :
    if d[now][isEarlier] != -1 :
        return d[now][isEarlier];

    IsVisited[now] = 1;
    tmp = 1 if isEarlier == 1 else 0;
    for next in Graph[now] :
        if IsVisited[next] :
            continue;
        if isEarlier == 1 :
            tmp += min(dfs(next, 1), dfs(next, 0));
        else :
            tmp += dfs(next, 1);
    IsVisited[now] = 0;

    d[now][isEarlier] = tmp;
    return d[now][isEarlier];

print(min(dfs(1, 1), dfs(1, 0)));