from collections import deque;

SIGNAL = deque([1,2,1,2,3,5]);
K = 5;

def check() :
    subSignal = deque([]);
    rtnCnt = 0;

    sum = 0;
    while SIGNAL:
        e = SIGNAL.popleft();
        sum += e;
        subSignal.append(e);
        if sum > K :
            mLeft = subSignal.popleft();
            sum -= mLeft;
        if sum == K :
            rtnCnt += 1;
    return rtnCnt;

print(check());