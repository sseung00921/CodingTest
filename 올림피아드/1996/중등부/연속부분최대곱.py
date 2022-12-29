import sys;
input = sys.stdin.readline;

n = int(input());
d = [[0] * 2 for _ in range(n + 2)];
data = [0];
for _ in range(n) :
    data.append(float(input()));

d[1][0] = 0;
d[1][1] = data[1];
for i in range(2, n + 1) :
    d[i][0] = max(d[i - 1][0], d[i - 1][1]);
    d[i][1] = max(d[i - 1][1] * data[i], data[i]);

print("{:.3f}".format(round(max(d[n][0], d[n][1]), 3)));