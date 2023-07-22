import sys;
input = sys.stdin.readline;
from bisect import bisect_left;

M, N, L = map(int, input().split());
Places = list(map(int, input().split()));
Animals = [];
for _ in range(N) :
    x, y = map(int, input().split())
    Animals.append([x, y]);

def checkIfIn(animalPos, placePos) :
    px, py = placePos, 0;
    ax, ay = animalPos;
    return abs(ax - px) + ay <= L;

Answer = 0;
Places.sort();
for animal in Animals :
    ax, ay = animal;
    placeIdx = bisect_left(Places, ax);
    if placeIdx == len(Places) :
        placeIdx = placeIdx - 1;
    elif placeIdx != 0 :
        if abs(ax - Places[placeIdx - 1]) < abs(ax - Places[placeIdx]) :
            placeIdx = placeIdx - 1;
    if checkIfIn((ax, ay), Places[placeIdx]) :
        Answer += 1;

print(Answer);
