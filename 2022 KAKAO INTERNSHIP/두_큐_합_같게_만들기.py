from collections import deque;

def solution(queue1, queue2):
    queue1 = deque(queue1);
    queue2 = deque(queue2);
    sumQ1 = sum(queue1);
    sumQ2 = sum(queue2);
    mid = sum(queue1) + sum(queue2);
    if mid % 2 == 1 :
        return -1;

    targetSum = mid // 2;
    if sumQ1 == targetSum and sumQ2 == targetSum :
        return 0;

    answer = 0;
    tryCnt = 3*(len(queue1) + len(queue2));
    while tryCnt > 0 :
        answer += 1;
        if sumQ1 > targetSum :
            eFromQ1 = queue1.popleft();
            queue2.append(eFromQ1);
            sumQ1 -= eFromQ1;
            sumQ2 += eFromQ1;
        else :
            eFromQ2 = queue2.popleft();
            queue1.append(eFromQ2);
            sumQ2 -= eFromQ2;
            sumQ1 += eFromQ2;
        if sumQ1 == sumQ2 :
            return answer;
        tryCnt -= 1;

    return -1;