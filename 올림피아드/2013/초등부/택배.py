import sys;
input = sys.stdin.readline;

N, C = map(int, input().split());
M = int(input());
Info = [];
for _ in range(M) :
    s, e, cnt = map(int, input().split());
    Info.append([s, e, cnt]);

Info.sort(key = lambda x : (x[1], -x[0]));
LoadingBoxCntInEachCity = [C] * (N + 1);
Answer = 0;
for element in Info :
    s, e, cnt = element;
    for i in range(s, e) :
        cnt = min(cnt, LoadingBoxCntInEachCity[i]);
    for i in range(s, e) :
        LoadingBoxCntInEachCity[i] -= cnt;
    Answer += cnt;

print(Answer);