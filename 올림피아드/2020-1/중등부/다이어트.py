import sys;
from itertools import combinations;

input = sys.stdin.readline;

MinCost = sys.maxsize;
MinCombination = None;
N = int(input());
Nedded = [0] + list(map(int, input().split()));
Foods = [];
for i in range(N) :
    Foods.append(([i + 1] + list(map(int, input().split()))));

def checkIfSatisfying(arr) :
    totalMp = 0; totalMf = 0; totalMs = 0; totalMv = 0;
    for e in arr :
        totalMp += e[1];
        totalMf += e[2];
        totalMs += e[3];
        totalMv += e[4];
    if totalMp >= Nedded[1] and totalMf >= Nedded[2] and totalMs >= Nedded[3] and totalMv >= Nedded[4] :
        return True;
    else :
        return False;

def tryRenewAnswer(arr) :
    global MinCost;
    global MinCombination;
    totalCost = 0;
    for e in arr :
        totalCost += e[5];
    if MinCombination == None or totalCost <= MinCost :
        renewedCombination = [];
        for e in arr :
            renewedCombination.append(e[0]);
        if totalCost < MinCost :
            MinCost = totalCost;
            MinCombination = sorted(renewedCombination);
        if totalCost == MinCost :
            tryMinCombination = sorted(renewedCombination);
            if tryMinCombination < MinCombination :
                MinCombination = tryMinCombination;

IsExist = False;
for i in range(1, N + 1) :
    for arr in combinations(Foods, i) :
        if checkIfSatisfying(arr) :
            IsExist = True;
            tryRenewAnswer(arr);

if not IsExist :
    print(-1);
else :
    print(MinCost);
    print(*MinCombination);
