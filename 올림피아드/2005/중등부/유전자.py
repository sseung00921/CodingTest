import sys;
input = sys.stdin.readline;

Strr = input().rstrip();
d = [[0] * len(Strr) for _ in range(len(Strr))]

def checker(start, end) :
    if Strr[start] == 'a' and Strr[end] == 't' or Strr[start] == 'g' and Strr[end] == 'c' :
        if end == start + 1 or end == start + 2:
            d[start][end] = 2;
        else :
            d[start][end] = max(d[start][end], d[start + 1][end - 1] + 2)
    for i in range(start, end) :
        d[start][end] = max(d[start][end], d[start][i] + d[i + 1][end]);
    return;

for k in range(1, len(Strr)) :
    for i in range(len(Strr)) :
        if i + k > len(Strr) - 1 :
            continue
        checker(i, i + k);

print(d[0][len(Strr) - 1]);
