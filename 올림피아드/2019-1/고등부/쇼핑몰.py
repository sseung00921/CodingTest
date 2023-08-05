import sys;
input = sys.stdin.readline;
import heapq;

N, K = map(int, input().split());
Info = [];
for _ in range(N) :
    id, load = map(int, input().split());
    Info.append((id, load));

q = [];
RstArrForEachTime = [[] for _ in range(N * 20 + 1)];
UsedCounter = 0;
for info in Info :
    givenId, givenLoad = info;
    if UsedCounter < K :
        heapq.heappush(q, (givenLoad, UsedCounter, givenId));
        UsedCounter += 1;
    else :
        firstLoad, firstCounter, firstId = heapq.heappop(q);
        heapq.heappush(q, (firstLoad + givenLoad, firstCounter, givenId));
        RstArrForEachTime[firstLoad].append(firstId);
while q :
    firstLoad, firstCounter, firstId = heapq.heappop(q);
    RstArrForEachTime[firstLoad].append(firstId);

RstArr = [];
for i in range(len(RstArrForEachTime)) :
    while RstArrForEachTime[i] :
        poppedVal = RstArrForEachTime[i].pop();
        RstArr.append(poppedVal);

Answer = 0;
for i in range(1, N + 1) :
    Answer += i*RstArr[i - 1];

print(Answer);
