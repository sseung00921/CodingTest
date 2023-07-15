import sys;
input = sys.stdin.readline;
from itertools import permutations;
Path = [1, 2, 3];
Cnts = [0] * 4;
N = int(input());
data = list(map(int, input().split()));
for e in data :
    Cnts[e] += 1;

Answer = int(1e11);
for order in list(permutations(Path, 3)) :
    valInEachPos = [[0] * 4 for _ in range(4)];
    step = 0;
    for i in order :
        for j in range(Cnts[i]) :
            valInEachPos[i][data[step + j]] += 1;
        step += Cnts[i];
    Answer = min(Answer, valInEachPos[1][2] + valInEachPos[1][3] + max(valInEachPos[2][3], valInEachPos[3][2]));
print(Answer);
