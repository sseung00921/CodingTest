import sys;
input = sys.stdin.readline;

N = int(input());
K = int(input());
d = [[-1] * (K + 1) for _ in range(N + 1)];
Mod = 1000000003;

def dfs(n, k) :
    if d[n][k] != -1 :
        return d[n][k];

    if n < k :
        d[n][k] = 0;
        return d[n][k];

    if k == 1 :
        d[n][k] = n;
        return d[n][k];

    if k == 0 :
        d[n][k] = 1;
        return d[n][k];

    if n <= 1 :
        d[n][k] = 0;
        return d[n][k];

    tmp = (dfs(n - 2, k - 1) + dfs(n - 1, k)) % Mod;
    d[n][k] = tmp;
    return d[n][k];

print((dfs(N - 3, K - 1) + dfs(N - 1, K) % Mod));

