def solution(stones, k):
    answer = 0;
    start = 0;
    end = 200000000;
    while start <= end :
        mid = (start + end) // 2;
        count = 0;
        for stone in stones :
            if stone - mid <= 0 :
                count += 1;
            else :
                count = 0;
            if count >= k :
                break;
        if count >= k :
            answer = mid;
            end = mid - 1;
        else :
            answer = mid + 1
            start = mid + 1;
    return answer;

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1];
k = 3;
print(solution(stones, k));