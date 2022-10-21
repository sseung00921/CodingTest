import sys;
sys.setrecursionlimit(10**5);
input = sys.stdin.readline;

MOD = 1000000003;
N = int(input());
k = int(input());
d = [[-1] * (k + 1) for _ in range(N + 1)]

def dfs(n, k) :
    if n < k :
        d[n][k] = 0;
        return 0;

    if k == 1 :
        d[n][k] = n;
        return n;

    if d[n][k] != -1 :
        return d[n][k];

    case1 = dfs(n - 1, k);
    case2 = dfs(n - 2, k - 1);
    d[n][k] = (case1 + case2) % MOD;

    return d[n][k];

answer = 0;
if k == 1 :
    answer = N;
else :
    answer = (dfs(N - 3, k - 1) + dfs(N - 1, k)) % MOD;
print(answer);