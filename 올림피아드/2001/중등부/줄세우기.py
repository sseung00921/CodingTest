import sys;
input = sys.stdin.readline;

n = int(input());
data = [];
for _ in range(n) :
    data.append(int(input()));

d = [1] * n;
for i in range(1, n) :
    for j in range(0, i) :
        if data[j] < data[i] :
            d[i] = max(d[i], d[j] + 1);

print(n - max(d));