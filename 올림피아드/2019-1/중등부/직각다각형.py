import sys;
input = sys.stdin.readline;

N = int(input());
Info = [];
for _ in range(N) :
    x, y = map(int, input().split());
    Info.append((x, y));

Seros = [];
Garos = [];
for i in range(len(Info) - 1) :
    if Info[i][0] == Info[i + 1][0] :
        Seros.append((min(Info[i][1], Info[i + 1][1]), max(Info[i][1], Info[i + 1][1])));
    else :
        Garos.append((min(Info[i][0], Info[i + 1][0]), max(Info[i][0], Info[i + 1][0])));
if Info[-1][0] == Info[0][0] :
    Seros.append((min(Info[-1][1], Info[0][1]), max(Info[-1][1], Info[0][1])));
else :
    Garos.append((min(Info[-1][0], Info[0][0]), max(Info[-1][0], Info[0][0])));

SerosCnts = [0] * (1000000 + 10);
GarosCnts = [0] * (1000000 + 10);
for sero in Seros :
    s, e = sero;
    s += 500000;
    e += 500000;
    SerosCnts[s + 1] += 1;
    SerosCnts[e] -= 1;
for garo in Garos :
    s, e = garo;
    s += 500000;
    e += 500000;
    GarosCnts[s + 1] += 1;
    GarosCnts[e] -= 1;

for i in range(1000000) :
    SerosCnts[i + 1] += SerosCnts[i];
    GarosCnts[i + 1] += GarosCnts[i];

print(max(max(GarosCnts), max(SerosCnts)));