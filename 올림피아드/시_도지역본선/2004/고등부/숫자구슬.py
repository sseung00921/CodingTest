import sys;
import math;
input = sys.stdin.readline;

n, m = map(int, input().split());
data = list(map(int, input().split()));

def splitWithTheNum(num) :
    rtnVal1 = 0;
    rtnVal2 = [];
    tmpSum = 0;
    tmpCnt = 0;
    for i in range(len(data)) :
        if tmpSum + data[i] > num :
            rtnVal1 += 1;
            rtnVal2.append(tmpCnt);
            tmpSum = data[i];
            tmpCnt = 1;
        else :
            tmpSum += data[i];
            tmpCnt += 1;
    if tmpCnt > 0 :
        rtnVal1 += 1;
        rtnVal2.append(tmpCnt);

    return rtnVal1, rtnVal2;

answer = int(1e11);
left = max(data); right = 30000002;
while left <= right :
    mid = (left + right) // 2
    cnt = splitWithTheNum(mid)[0];
    if cnt <= m:
        answer = min(answer, mid);
        right = mid - 1
    elif cnt > m:
        left = mid + 1


print(answer);
ansList = splitWithTheNum(answer)[1];
while len(ansList) < m :
    for i in range(len(ansList)) :
        if ansList[i] > 1 :
            tmp1 = ansList[i];
            del ansList[i];
            tmp2 = math.floor(tmp1 / 2);
            tmp3 = math.ceil(tmp1 / 2);
            ansList.insert(i, tmp2);
            ansList.insert(i, tmp3);
            break;
print(*ansList);