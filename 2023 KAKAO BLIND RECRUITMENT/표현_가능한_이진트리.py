import math;

def customBin(num) :
    tmpStr = bin(num)[2 : ];
    logRst = int(math.log(len(tmpStr), 2)) + 1;
    reqLen = 2**logRst - 1;
    tmpStr = tmpStr.zfill(reqLen)
    return tmpStr;

def dfs(strBin, left, right, strSize) :
    if strSize == 1 :
        return 1;

    mid = (left + right) // 2;
    leftRoot = (left + mid - 1) // 2;
    rightRoot = (mid + 1 + right) // 2;

    if strBin[mid] == '0' and (strBin[leftRoot] == '1' or strBin[rightRoot] == '1') :
        return 0;
    else :
        if dfs(strBin, left, mid - 1, strSize // 2) == 0 :
            return 0;
        if dfs(strBin, mid + 1, right, strSize // 2) == 0 :
            return 0;
    return 1;

def solution(numbers):
    answer = [];
    for num in numbers :
        strBin = customBin(num);
        answer.append(dfs(strBin, 0, len(strBin) - 1, len(strBin)));
    return answer

numbers = [63, 111, 95];
print(solution(numbers));
print(customBin(42))

