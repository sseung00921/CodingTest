def solution(dartResult):
    scores = [];
    num = ''
    score = 0;
    for c in dartResult :
        if c.isnumeric() :
            num += c;
        elif c == 'S':
            score = int(num);
            scores.append(score);
            num = '';
        elif c == 'D':
            score = int(num)**2;
            scores.append(score);
            num = '';
        elif c == 'T' :
            score = int(num)**3;
            scores.append(score);
            num = '';
        elif c == '#' :
            scores[-1] *= -1;
        elif c == '*' :
            scores[-1] *= 2;
            if len(scores) > 1 :
                scores[-2] *= 2;

    answer = sum(scores);
    return answer

dartResult = "1S2D*3T";
print(solution(dartResult));
