import sys;
input = sys.stdin.readline;

t = int(input());
k = int(input());
data = [];
for _ in range(k) :
    data.append(list(map(int, input().split())));

d = [[-1] * (t + 1) for _ in range(k + 1)];

def dfs(covered, remain) :
    if remain == 0 :
        d[covered][remain] = 1;
        return d[covered][remain];

    if covered == k :
        d[covered][remain] = 0;
        return d[covered][remain]

    if d[covered][remain] != -1 :
        return d[covered][remain];

    d[covered][remain] = 0;
    value, cnt = data[covered];
    d[covered][remain] += dfs(covered + 1, remain);
    for i in range(1, cnt + 1) :
        if remain - i*value >= 0 :
            d[covered][remain] += dfs(covered + 1, remain - i*value);

    return d[covered][remain];

print(dfs(0, t));
