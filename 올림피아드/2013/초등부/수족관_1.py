import sys;
input = sys.stdin.readline;

N = int(input());
Points = [];
Seros = [];
Garos = [];
for _ in range(N) :
    x, y = map(int, input().split());
    Points.append([x, y]);
Punks = [];
K = int(input());
for _ in range(K) :
    Punks.append(list(map(int, input().split())));
for i in range(1, N) :
    if i % 2 == 1 :
        sx, sy = Points[i - 1];
        ex, ey = Points[i];
        height = ey;
        Seros.append([sx, sy, ex, ey, height]);
    else :
        sx, sy = Points[i - 1];
        ex, ey = Points[i];
        coverWidthStart = min(sx, ex);
        coverWidthEnd = max(sx, ex);
        Garos.append([sx, sy, ex, ey, coverWidthStart, coverWidthEnd]);

CheckNowRemoved = [0] * (len(Seros) - 1);

TotalLitterWhenStart = 0;
for i in range(0, len(Seros) - 1) :
    height = Seros[i][4];
    weight = Garos[i][5] - Garos[i][4];
    TotalLitterWhenStart += weight*height;

PunkedIdxes = [];
for i in range(len(Garos)) :
    for p in Punks :
        if p == Garos[i][ : 4] :
            PunkedIdxes.append(i);
            break;

for punkedIdx in PunkedIdxes :
    startHeight = Seros[punkedIdx][4];
    for left in range(punkedIdx, -1, -1) :
        if Seros[left][4] >= startHeight :
            CheckNowRemoved[left] = max(CheckNowRemoved[left], startHeight);
        elif Seros[left][4] < startHeight :
            CheckNowRemoved[left] = max(CheckNowRemoved[left], Seros[left][4]);
            startHeight = Seros[left][4];
    startHeight = Seros[punkedIdx][4];
    for right in range(punkedIdx + 1, len(Seros) - 1) :
        if Seros[right][4] >= startHeight :
            CheckNowRemoved[right] = max(CheckNowRemoved[right], startHeight);
        elif Seros[right][4] < startHeight :
            CheckNowRemoved[right] = max(CheckNowRemoved[right], Seros[right][4]);
            startHeight = Seros[right][4];

AmountToSubtract = 0;
for i in range(len(CheckNowRemoved)) :
    AmountToSubtract += CheckNowRemoved[i]*(Garos[i][5] - Garos[i][4]);

print(TotalLitterWhenStart - AmountToSubtract);