import sys;
input = sys.stdin.readline;

from collections import deque;

criLen = int(input());
criterion = list(map(int, input().split()));

n = int(input());
data = [];
for _ in range(n) :
    data.append(tuple(map(int, input().split())));

def makeReverse(criterion) :
    reverseCriterion = [];
    for order in criterion[::-1] :
        if order == 2 :
            reverseCriterion.append(4);
        elif order == 4 :
            reverseCriterion.append(2);
        elif order == 3 :
            reverseCriterion.append(1);
        elif order == 1 :
            reverseCriterion.append(3);
    return reverseCriterion;

def constructSet(shapeArr) :
    rpeatedCnt = 0;
    q = deque(shapeArr);
    while rpeatedCnt < criLen :
        possibleSet.add(tuple(list(q)));
        e = q.popleft();
        q.append(e);
        rpeatedCnt += 1;
    return;

possibleSet = set();
reverseCriterion = makeReverse(criterion);
constructSet(criterion);
constructSet(reverseCriterion);

ansCnt = 0;
ansArr = [];
for e in data :
    if e in possibleSet :
        ansCnt += 1;
        ansArr.append(e);

print(ansCnt);
for e in ansArr :
    print(*e);