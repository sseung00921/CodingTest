import sys;
input = sys.stdin.readline;
import heapq;

N, M = map(int, input().split());
Info = [];
hq = [];
for _ in range(N) :
    Info.append(list(map(int, input().split())));

for i in range(N) :
    Info[i].sort();

ToSearchStudentIdxArr = [0] * N;
NowMax = -1;
for i in range(N) :
    heapq.heappush(hq, (Info[i][0], i));
    NowMax = max(NowMax, Info[i][0]);

Answer = int(1e10);
while True :
    nowMin, nowClassIdx = heapq.heappop(hq);
    Answer = min(Answer, NowMax - nowMin);
    if ToSearchStudentIdxArr[nowClassIdx] == M - 1 :
        break;
    ToSearchStudentIdxArr[nowClassIdx] += 1;
    heapq.heappush(hq, (Info[nowClassIdx][ToSearchStudentIdxArr[nowClassIdx]], nowClassIdx));
    NowMax = max(NowMax, Info[nowClassIdx][ToSearchStudentIdxArr[nowClassIdx]]);

print(Answer);
