from collections import deque;
N = 0; M = 0;

def solution(rc, operations):
    global N; global M;
    N = len(rc); M = len(rc[0]);

    rc = deque(rc);

    leftQ = deque([]);
    rightQ = deque([]);
    for i in range(0, N) :
        leftQ.append(rc[i][0]);
        rightQ.append(rc[i][M - 1]);

    for i in range(N) :
        rc[i] = deque(rc[i][1 : -1]);

    for op in operations :
        if op == "ShiftRow" :
            rc.appendleft(rc.pop());
            leftQ.appendleft(leftQ.pop());
            rightQ.appendleft(rightQ.pop())
        elif op == "Rotate" :
            topQ = rc[0];
            bottomQ = rc[-1];
            if len(topQ) > 0 :
                topQ.appendleft(leftQ.popleft());
                leftQ.append(bottomQ.popleft());
                bottomQ.append(rightQ.pop());
                rightQ.appendleft(topQ.pop());
            elif len(topQ) == 0 :
                leftQ.append(rightQ.pop());
                rightQ.appendleft(leftQ.popleft());

    answer = [[0] * M for _ in range(N)];
    for i in range(N) :
        answer[i][0] = leftQ[i];
        answer[i][M - 1] = rightQ[i];
    for i in range(N) :
        for j in range(1, M - 1) :
            answer[i][j] = rc[i][j - 1];
    return answer

rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]];
operation = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
print(solution(rc, operation));