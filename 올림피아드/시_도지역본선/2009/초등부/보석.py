import sys;
input = sys.stdin.readline;

N, M, T, K = map(int, input().split());
poses = [];
for _ in range(T) :
    a, b = map(int, input().split());
    poses.append((a, b));

poses.sort();

AnswerX = -1;
AnswerY = -1;
Answer = -1;
def countMine(sx, sy) :
    global AnswerX;
    global AnswerY;
    global Answer;

    ex = sx + K;
    ey = sy + K;

    if ex > N :
        ex = N; sx = N - K;
    if ey > M :
        ey = M; sy = M - K;

    tmpCnt = 0;
    for p in poses :
        px, py = p;
        if sx <= px <= ex and sy <= py <= ey :
            tmpCnt += 1;
    if tmpCnt > Answer :
        AnswerX = sx;
        AnswerY = ey;
        Answer = tmpCnt;
    return;

for idx1 in range(len(poses)) :
    x1, y1 = poses[idx1];
    startX = x1;
    for idx2 in range(idx1, len(poses)) :
        x2, y2 = poses[idx2];
        if x2 - startX > K :
            break;
        countMine(x1, y1);
        countMine(x1, max(0, y1 - K));
        if abs(y2 - y1) <= K :
            if y2 <= y1 :
                countMine(x1, y2);
            else :
                countMine(x1, max(0, y2 - K));

print(AnswerX, AnswerY);
print(Answer);