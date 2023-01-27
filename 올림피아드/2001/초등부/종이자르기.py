import sys;
input = sys.stdin.readline;

w, h = map(int, input().split());
n = int(input());
wCuts = [0];
hCuts = [0];
for _ in range(n) :
    kind, num = map(int, input().split())
    if kind == 0 :
        wCuts.append(num);
    elif kind == 1 :
        hCuts.append(num);
wCuts.append(h);
hCuts.append(w);
wCuts.sort();
hCuts.sort();

wParts = [];
hParts = [];
for i in range(1, len(wCuts)) :
    wParts.append(wCuts[i] - wCuts[i - 1]);
for i in range(1, len(hCuts)) :
    hParts.append(hCuts[i] - hCuts[i - 1]);

maxArea = -1;
for i in range(len(wParts)) :
    for j in range(len(hParts)) :
        maxArea = max(maxArea, wParts[i]*hParts[j]);
print(maxArea)