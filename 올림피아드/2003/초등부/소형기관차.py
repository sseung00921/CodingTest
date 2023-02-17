import sys;
input = sys.stdin.readline;

n = int(input());
data = list(map(int, input().split()));
limit = int(input());

S = [0];
for i in range(1, n + 1) :
    S.append(S[i - 1] + data[i - 1]);
d = [[0] * (n + 1) for _ in range(4)]

for i in range(1, 4) :
    for j in range(1, n + 1) :
        if i == 1 :
            if j < limit :
                continue;
            d[1][j] = max(d[1][j - 1], S[j] - S[j - limit]);
        else :
            if j < limit :
                continue;
            d[i][j] = max(d[i][j - 1], d[i - 1][j - limit] + S[j] - S[j - limit]);

print(d[3][n]);