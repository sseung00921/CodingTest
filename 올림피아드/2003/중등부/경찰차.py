import sys;
input = sys.stdin.readline;

n = int(input());
w = int(input());
cases = [0];
car1Start = (1, 1);
car2Start = (n, n);
d = [[-1] * (w + 1) for _ in range(w + 1)];
for i in range(w) :
    r, c = map(int, input().split());
    cases.append((r, c));

def calDistance(carPos, targetCasePos) :
    carR, carC = carPos;
    tarR, tarC = targetCasePos
    return abs(carR - tarR) + abs(carC - tarC);

def dfs(car1CoveredNum, car2CoveredNum, coveredCaseNum) :
    if coveredCaseNum == w :
        return 0;
    if d[car1CoveredNum][car2CoveredNum] != -1 :
        return d[car1CoveredNum][car2CoveredNum];

    coveredCaseNum = max(car1CoveredNum, car2CoveredNum);
    targetCaseNum = coveredCaseNum + 1;
    if car1CoveredNum == 0 :
        car1Dist = calDistance(car1Start, cases[targetCaseNum]);
    else :
        car1Dist = calDistance(cases[car1CoveredNum], cases[targetCaseNum]);
    if car2CoveredNum == 0 :
        car2Dist = calDistance(car2Start, cases[targetCaseNum]);
    else :
        car2Dist = calDistance(cases[car2CoveredNum], cases[targetCaseNum]);

    distWhenCar1GoTargetCaseNum = car1Dist + dfs(targetCaseNum, car2CoveredNum, targetCaseNum);
    distWhenCar2GoTargetCaseNum = car2Dist + dfs(car1CoveredNum, targetCaseNum, targetCaseNum);

    totalDist = min(distWhenCar1GoTargetCaseNum, distWhenCar2GoTargetCaseNum);

    d[car1CoveredNum][car2CoveredNum] = totalDist;
    return d[car1CoveredNum][car2CoveredNum];

def trackPath(car1CoveredNum, car2CoveredNum, coveredCaseNum, pathArr) :
    if len(pathArr) == w :
        return pathArr;

    coveredCaseNum = max(car1CoveredNum, car2CoveredNum);
    targetCaseNum = coveredCaseNum + 1;

    if car1CoveredNum == 0 :
        car1Dist = calDistance(car1Start, cases[targetCaseNum]);
    else :
        car1Dist = calDistance(cases[car1CoveredNum], cases[targetCaseNum]);
    if car2CoveredNum == 0 :
        car2Dist = calDistance(car2Start, cases[targetCaseNum]);
    else :
        car2Dist = calDistance(cases[car2CoveredNum], cases[targetCaseNum]);

    distWhenCar1GoTargetCaseNum = car1Dist + dfs(targetCaseNum, car2CoveredNum, targetCaseNum);
    distWhenCar2GoTargetCaseNum = car2Dist + dfs(car1CoveredNum, targetCaseNum, targetCaseNum);

    if distWhenCar1GoTargetCaseNum < distWhenCar2GoTargetCaseNum :
        pathArr.append(1);
        return trackPath(targetCaseNum, car2CoveredNum, targetCaseNum, pathArr);
    else :
        pathArr.append(2)
        return trackPath(car1CoveredNum, targetCaseNum, targetCaseNum, pathArr);

print(dfs(0, 0, 0));
path = trackPath(0, 0, 0, []);
for e in path :
    print(e);
