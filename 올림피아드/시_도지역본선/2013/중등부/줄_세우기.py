import sys;
input = sys.stdin.readline;

N = int(input());
Data = list(map(int, input().split()));
ValToIdxMap = dict();

for idx, val in enumerate(Data) :
    ValToIdxMap[val] = idx;

MaxLen = 1;
NowLen = 1;
for num in range(1, N) :
    if ValToIdxMap[num] < ValToIdxMap[num + 1] :
        NowLen += 1;
        MaxLen = max(MaxLen, NowLen);
    else :
        NowLen = 1;

print(N - MaxLen);