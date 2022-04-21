def toNJinsuStr(n, num) :
    mapper = dict();
    mapper[10] = 'A';
    mapper[11] = 'B';
    mapper[12] = 'C';
    mapper[13] = 'D';
    mapper[14] = 'E';
    mapper[15] = 'F';

    rtnStr = '';

    while True :
        mod = num % n;
        if mod >= 10 :
            rtnStr = mapper[mod] + rtnStr;
        else :
            rtnStr = str(mod) + rtnStr;
        num //= n;
        if num == 0 :
            break;

    return rtnStr;


def solution(n, t, m, p):
    maxLen = m * t;
    nextNumToTrans = 0;
    totalStr = '';
    while True :
        transedStr = toNJinsuStr(n, nextNumToTrans);
        totalStr += transedStr;
        if len(totalStr) >= maxLen :
            break;
        nextNumToTrans += 1;

    answer = ''
    for i in range(p - 1, len(totalStr), m) :
        answer += totalStr[i];
        if len(answer) >= t :
            break;

    return answer

n = 2;
t = 4;
m = 2;
p = 1;
print(solution(n, t, m, p));