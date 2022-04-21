n, m = map(int, input().split());
kind = [];
d = [-1] * (m + 1);

for _ in range(n) :
    danwi = int(input());
    kind.append(danwi);
    if danwi <= m :
        d[danwi] = 1;

for i in range(1, m + 1) :
    for danwi in kind :
        if i - danwi < 0 :
            continue;
        if d[i - danwi] == -1 :
            continue;
        if d[i] == -1 :
            d[i] = d[i - danwi] + 1;
        else :
            d[i] = min(d[i - danwi] + 1, d[i]);
print(d[m]);