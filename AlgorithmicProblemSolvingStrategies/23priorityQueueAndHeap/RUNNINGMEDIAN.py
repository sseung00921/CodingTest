import heapq;

A = None;
N = 0;
SUM = 0;

tc = int(input());
while tc > 0 :
    N, a, b = map(int, input().split());
    SUM = 0;
    A = [None] * N;
    A[0] = 1983;
    for i in range(1, N) :
        A[i] = (A[i - 1]*a + b)%20090711;
    maxHeap = [];
    minHeap = [];
    for i in range(N) :
        if len(maxHeap) == len(minHeap) :
            heapq.heappush(maxHeap, -A[i]);
        else :
            heapq.heappush(minHeap, A[i]);
        if len(maxHeap) > 0 and len(minHeap) > 0  and abs(maxHeap[0]) > minHeap[0] :
            a = heapq.heappop(maxHeap);
            b = heapq.heappop(minHeap);
            heapq.heappush(minHeap, -a);
            heapq.heappush(maxHeap, -b);
        SUM += abs(maxHeap[0]);
    print(SUM % 20090711);
    tc -= 1;