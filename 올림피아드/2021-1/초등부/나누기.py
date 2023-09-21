import sys;
sys.setrecursionlimit(100010)

input = sys.stdin.readline;
N = int(input());
Arr = list(map(int, input().split()));
Sum = sum(Arr);
if Sum % 4 != 0 :
    print(0);
    sys.exit();

K = Sum // 4;

Cum = [0] * N;
Cum[0] = Arr[0];
for i in range(1, N) :
    Cum[i] = Cum[i - 1] + Arr[i];

d = [[-1] * 4 for _ in range(N + 1)];
def dfs(idx, cnt) :
    if idx == N :
        return 0;

    if cnt == 3 :
        return 1;

    if d[idx][cnt] != -1 :
        return d[idx][cnt];

    d[idx][cnt] = 0;
    if Cum[idx] == (cnt + 1) * K :
        d[idx][cnt] += dfs(idx + 1, cnt + 1);
        d[idx][cnt] += dfs(idx + 1, cnt);
    else :
        d[idx][cnt] += dfs(idx + 1, cnt);
    return d[idx][cnt];

print(dfs(0, 0));