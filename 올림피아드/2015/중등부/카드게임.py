import sys;
input = sys.stdin.readline;
sys.setrecursionlimit(10**4);

N = int(input());
Left = list(map(int, input().split()));
Right = list(map(int, input().split()));
Left = [0] + Left[::-1];
Right = [0] + Right[::-1];
d = [[-1] * (N + 1) for _ in range(N + 1)];

def dfs(leftRemain, rightRemain) :
    if d[leftRemain][rightRemain] != -1 :
        return d[leftRemain][rightRemain];

    if leftRemain == 0 or rightRemain == 0 :
        d[leftRemain][rightRemain] = 0;
        return d[leftRemain][rightRemain];

    possible1 = dfs(leftRemain - 1, rightRemain);
    possible2 = dfs(leftRemain - 1, rightRemain - 1);
    possible3 = -1;
    if Right[rightRemain] < Left[leftRemain] :
        possible3 = Right[rightRemain] + dfs(leftRemain, rightRemain - 1);

    d[leftRemain][rightRemain] = max(possible1, possible2, possible3);
    return d[leftRemain][rightRemain];

dfs(N, N);
print(d[N][N]);