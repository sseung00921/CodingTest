import sys;
input = sys.stdin.readline;

MOD = int(1e9) + 9;
N, K = map(int, input().split());
d = [1] * (N + 1);
for i in range(1, N +1) :
    d[i] = d[i - 1]*K;
    if i >= 5 :
        d[i] -= 2*d[i - 5];
    if i >= 7 :
        d[i] += d[i - 7];
    d[i] %= MOD;

print(d[N]);
