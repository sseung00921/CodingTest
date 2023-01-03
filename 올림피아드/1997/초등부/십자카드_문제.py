import sys;
input = sys.stdin.readline;

alltimeNumList = [];
alltimeNumSet = set();

def makeTimeNum(numArr) :
    firstCase = numArr[0]*1000 + numArr[1]*100 + numArr[2]*10 + numArr[3];
    secondCase = numArr[1]*1000 + numArr[2]*100 + numArr[3]*10 + numArr[0];
    thirdCase = numArr[2]*1000 + numArr[3]*100 + numArr[0]*10 + numArr[1];
    fourthCase = numArr[3]*1000 + numArr[0]*100 + numArr[1]*10 + numArr[2];
    return min(firstCase, secondCase, thirdCase, fourthCase);

for a in range(1, 10) :
    for b in range(1, 10) :
        for c in range(1, 10) :
            for d in range(1, 10) :
                timeNum = makeTimeNum([a, b, c, d])
                if timeNum not in alltimeNumSet :
                    alltimeNumSet.add(timeNum);
                    alltimeNumList.append(timeNum);

ta, tb, tc, td = map(int, input().split());
targetNum = makeTimeNum([ta, tb, tc, td]);
print(alltimeNumList.index(targetNum) + 1);