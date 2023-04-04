import sys;
input = sys.stdin.readline;

R, C = map(int, input().split());
target = int(input());
f = int(input());
poses = [];

maxHeight = -1;
for _ in range(f) :
    r, c = map(int, input().split())
    maxHeight = max(maxHeight, r);
    poses.append((r, c));

poses.sort(key = lambda x : x[1]);

def getMinimumNeededCnt(size) :
    startC = poses[0][1];
    canCoverC = startC + size - 1;

    rtnCnt = 1;
    for i in range(f) :
        if poses[i][1] <= canCoverC :
            continue;
        else :
            rtnCnt += 1;
            startC = poses[i][1];
            canCoverC = startC + size - 1;

    return rtnCnt;

left = maxHeight;
right = 1000000;

answer = right + 1;
while left <= right :
    mid = (left + right) // 2
    if getMinimumNeededCnt(mid) > target :
        left = mid + 1;
    elif getMinimumNeededCnt(mid) <= target:
        answer = min(answer, mid);
        right = mid - 1;

print(answer);

