import sys;
input = sys.stdin.readline;

N = int(input());
def customBin(N) :
    rtnVal = bin(N)[2 : ];
    if rtnVal[0] == '1' :
        rtnVal = '0' + rtnVal;
    return rtnVal;

def getNearlestSmall(binN) :
    givenList = list(binN);
    canCnovert = False;
    cuttingStartIdx = -1;
    oneCount = 0;
    for i in range(len(givenList) - 1, 0, -1) :
        if givenList[i] == '0' and givenList[i - 1] == '1' :
            cuttingStartIdx = i + 1;
            givenList[i], givenList[i - 1] = givenList[i - 1], givenList[i];
            canCnovert = True;
            break;
        else :
            if givenList[i] == '1' :
                oneCount += 1;
    if canCnovert :
        tmpArr = ['0'] * (len(givenList) - cuttingStartIdx);
        for i in range(0, len(tmpArr)) :
            if oneCount == 0 :
                break;
            tmpArr[i] = '1';
            oneCount -= 1;
        rstBin = ''.join(givenList)[ : cuttingStartIdx] + ''.join(tmpArr);
        return int(rstBin, 2);
    else:
        return 0;

def getNearlestBig(binN) :
    givenList = list(binN);
    canCnovert = False;
    cuttingStartIdx = -1;
    oneCount = 0;
    for i in range(len(givenList) - 1, 0, -1) :
        if givenList[i] == '1' and givenList[i - 1] == '0' :
            cuttingStartIdx = i + 1
            givenList[i], givenList[i - 1] = givenList[i - 1], givenList[i];
            canCnovert = True;
            break;
        else :
            if givenList[i] == '1' :
                oneCount += 1;
    if canCnovert :
        tmpArr = ['0'] * (len(givenList) - cuttingStartIdx);
        for i in range(len(tmpArr) - 1, -1, -1) :
            if oneCount == 0 :
                break;
            tmpArr[i] = '1';
            oneCount -= 1;
        rstBin = ''.join(givenList)[ : cuttingStartIdx] + ''.join(tmpArr);
        return int(rstBin, 2);
    else:
        return 0;

binN = customBin(N);
print(getNearlestSmall(binN), getNearlestBig(binN));