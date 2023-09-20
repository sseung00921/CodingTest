import sys;
from bisect import bisect_right;

input = sys.stdin.readline;
S = input().rstrip();
T = input().rstrip();
TArr = [[] for _ in range(26)];
for i in range(len(T)) :
    TArr[ord(T[i]) - ord('a')].append(i);

def solve() :
    answer = 1;
    nowPos = -1;
    for i in range(len(S)) :
        k = ord(S[i]) - ord('a');
        if not TArr[k] :
            return -1;
        else :
            nowPos = bisect_right(TArr[k], nowPos);
            if nowPos == len(TArr[k]) :
                answer += 1;
                nowPos = 0;
            nowPos = TArr[k][nowPos];
    return answer;

print(solve());

