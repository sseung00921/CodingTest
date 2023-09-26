import sys;

input = sys.stdin.readline;
N = int(input());
Arr = [0] + list(map(int, input().split()));

CheckIfOnlyTwoUse = [[0] * (N + 1) for _ in range(N + 1)];
for end in range(N, -1, -1) :
    right = Arr[end];
    for start in range(end - 1, -1, -1) :
        left = Arr[start];
        if left < right :
            break;
        if left == right :
            CheckIfOnlyTwoUse[start][end] = 1;
            break;
        right = left - right;

INF = sys.maxsize;
d = [INF] * (N + 1);
d[0] = 0;
d[1] = 1;
for end in range(2, N + 1) :
    d[end] = d[end - 1] + 1;
    for start in range(end - 1, -1, -1) :
        if CheckIfOnlyTwoUse[start][end] :
            d[end] = min(d[end], d[start - 1] + (end - start));
            break;

print(d[N]);