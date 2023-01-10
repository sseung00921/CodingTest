import sys;
input = sys.stdin.readline;
import heapq;

n = int(input());
a, b = map(int, input().split());
reqCnt = int(input());
reqArr = [];
answer = int(1e9);

for _ in range(reqCnt) :
    reqArr.append(int(input()));

startBitMask = 0;
for num in range(1, n + 1) :
    if num == a or num == b :
        continue;
    else :
        startBitMask |= 1 << (num - 1);

answer = int(1e9);
q = [];
heapq.heappush(q, (0, startBitMask, 0));
while q :
    nowMovedCnt, nowBitMask, nowCoveredCnt = heapq.heappop(q);
    if nowCoveredCnt == reqCnt :
        answer = nowMovedCnt;
        break;

    cabToOpen = reqArr[nowCoveredCnt] - 1;

    if nowBitMask & (1 << cabToOpen) == 0 :
        q.append((nowMovedCnt, nowBitMask, nowCoveredCnt + 1));
    else :
        if cabToOpen == 0 :
            idx = -1;
            for i in range(1, n) :
                if nowBitMask & (1 << i) == 0 :
                    idx = i;
                    break;
            movedDistance = idx;
            nextBitMask = nowBitMask | (1 << idx);
            nextBitMask = nextBitMask & ~(1 << cabToOpen);
            heapq.heappush(q, (nowMovedCnt + movedDistance, nextBitMask, nowCoveredCnt + 1));
        elif cabToOpen == n - 1 :
            idx = -1;
            for i in range(n - 2, -1, -1) :
                if nowBitMask & (1 << i) == 0 :
                    idx = i;
                    break;
            movedDistance = (n - 1) - idx;
            nextBitMask = nowBitMask | (1 << idx);
            nextBitMask = nextBitMask & ~(1 << cabToOpen);
            heapq.heappush(q, (nowMovedCnt + movedDistance, nextBitMask, nowCoveredCnt + 1));
        elif 0 < cabToOpen < n - 1 :
            idx = -1;
            for i in range(cabToOpen + 1, n) :
                if nowBitMask & (1 << i) == 0 :
                    idx = i;
                    break;
            if idx != -1 :
                movedDistance = idx - cabToOpen;
                nextBitMask = nowBitMask | (1 << idx);
                nextBitMask = nextBitMask & ~(1 << cabToOpen);
                heapq.heappush(q, (nowMovedCnt + movedDistance, nextBitMask, nowCoveredCnt + 1));

            idx = -1;
            for i in range(cabToOpen - 1, -1, -1) :
                if nowBitMask & (1 << i) == 0 :
                    idx = i;
                    break;
            if idx != -1 :
                movedDistance = cabToOpen - idx;
                nextBitMask = nowBitMask | (1 << idx);
                nextBitMask = nextBitMask & ~(1 << cabToOpen);
                heapq.heappush(q, (nowMovedCnt + movedDistance, nextBitMask, nowCoveredCnt + 1));
print(answer);