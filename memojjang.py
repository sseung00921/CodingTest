import sys;
input = sys.stdin.readline;
s = ' ' + input().strip();
l = len(s);
d = [2500] * (l + 1);
isPal = [[0] * (l + 1) for _ in range(l + 1)];

for i in range(1, l) :
    isPal[i][i] = 1;

for i in range(2, l) :
    if s[i - 1] == s[i] :
        isPal[i - 1][i] = 1;

for size in range(3, l) :
    for start in range(l - size + 1) :
        end = start + size - 1;
        if s[start] == s[end] and isPal[start + 1][end - 1] :
            isPal[start][end] = 1;

d[0] = 0;
for end in range(1, l) :
    d[end] = min(d[end], d[end - 1] + 1);
    for start in range(1, end) :
        if isPal[start][end] :
            d[end] = min(d[end], d[start - 1] + 1);

print(d[l - 1]);
