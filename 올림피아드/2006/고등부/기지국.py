import sys;
input = sys.stdin.readline;

n = int(input());
INF = int(1e9);
poses = [(-INF, -INF)];
for _ in range(n) :
    x, y = map(int, input().split());
    poses.append((x, y));

poses.sort(key = lambda x : x[0]);
d = [INF] * (n + 1);
d[0] = 0;
d[1] = 2*abs(poses[1][1]);

for i in range(2, n + 1) :
    d[i] = min(d[i], d[i - 1] + 2*abs(poses[i][1]));
    highest = abs(poses[i][1]);
    for j in range(i - 1, 0, -1) :
        highest = max(highest, abs(poses[j][1]));
        widest = poses[i][0] - poses[j][0];
        cost = max(widest, 2*highest);
        d[i] = min(d[i], d[j - 1] + cost);

print(d[n]);
