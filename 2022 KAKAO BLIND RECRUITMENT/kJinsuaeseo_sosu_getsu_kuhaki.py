def solution(n, k):
    strKBasedN = '';
    while n > 0 :
        strKBasedN = str((n % k)) + strKBasedN;
        n //= k;

    nums = strKBasedN.split("0");

    answer = 0;
    for num in nums :
        if len(num) == 0 :
            continue;
        if int(num) == 1 :
            continue;
        else :
            sosu = True;
            for i in range(2, int(int(num)**0.5) + 1) :
                if int(num) % i == 0 :
                    sosu = False;
                    break;
            if sosu == True :
                answer += 1;
    return answer

n = 437674;
k = 3;
print(solution(n, k));
n = 110011;
k = 10;
print(solution(n, k));