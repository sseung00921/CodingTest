N = 0;
K = 0;
A = None;
SIGNAL = None;
CNT = 0;

def check() :
    leftIdx = 0;
    rightIdx = 0;
    rtnCnt = 0;

    sum = 0;
    while rightIdx < len(SIGNAL) :
        if sum <= K :
            if sum == K :
                rtnCnt += 1;
            sum += SIGNAL[rightIdx];
            rightIdx += 1;
        elif sum > K :
            sum -= SIGNAL[leftIdx];
            leftIdx += 1;

    return rtnCnt;

tc = int(input());
while tc > 0 :
    K, N = map(int, input().split());
    A = [-1] * N;
    A[0] = 1983;
    for i in range(1, N) :
        A[i] = ((A[i - 1]*214013 + 2531011) % 2**32)
    SIGNAL = [-1] * (N);
    for i in range(N) :
        SIGNAL[i] = A[i] % 10000 + 1;
    print(check());
    tc -= 1;