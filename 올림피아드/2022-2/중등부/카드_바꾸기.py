import sys;

input = sys.stdin.readline;
N = int(input());
Arr = list(map(int, input().split()));

Answer = N;
def calNeededChangeCnt(criIdx, step) :
    answer = 0;
    startNum = Arr[criIdx];
    for i in range(criIdx - 1, -1, -1) :
        startNum -= step;
        if Arr[i] != startNum :
            answer += 1;
    startNum = Arr[criIdx];
    for i in range(criIdx + 1, len(Arr)) :
        startNum += step;
        if Arr[i] != startNum :
            answer += 1;
    return answer;

for i in range(N) :
    for j in range(i + 1, N) :
        diff = abs(Arr[j] - Arr[i]);
        if diff % (j - i) != 0 :
            continue;
        step = diff // (j - i) if Arr[j] >= Arr[i] else -(diff // (j - i));
        Answer = min(Answer, calNeededChangeCnt(i, step));

print(Answer);