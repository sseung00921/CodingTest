import sys;
input = sys.stdin.readline;
from collections import deque;

n = int(input());
m = int(input());
recomendedOrder = list(map(int, input().split()));

def findIdxByStudentNum(arr, studentNum) :
    for i in range(len(arr)) :
        if arr[i][0] == studentNum :
            return i;
    return -1;

q = deque([]);

for i in range(m) :
    idx = findIdxByStudentNum(q, recomendedOrder[i]);
    if idx >= 0 :
        q[idx][2] += 1;
    else :
        if len(q) < n :
            q.append([recomendedOrder[i], i + 1, 1]);
        else :
            sortedTempArr = sorted(q, key= lambda x : (x[2], x[1]));
            studentToPop = sortedTempArr[0][0];
            studentToPopIdx = findIdxByStudentNum(q, studentToPop);
            q[studentToPopIdx] = [recomendedOrder[i], i + 1, 1];

answer = [];
while q :
    studentNum = q.popleft()[0];
    answer.append(studentNum);
answer.sort();
print(*answer);
