import sys;
input = sys.stdin.readline;

a, b, d, N = map(int, input().split());
dp = [0] * (N + 1);

DIV = 1000;
dp[0] = 1;

for i in range(1, N + 1) :
    if i < a :
        dp[i] = 1;
    else :
        if i < b :
            dp[i] = (dp[i - 1] + dp[i - a]) % DIV;
        else :
            dp[i] = (dp[i - 1] + dp[i - a] - dp[i - b] + DIV) % DIV;

if N < d :
    print(dp[N]);
else :
    print((dp[N] - dp[N - d] + DIV) % DIV);

