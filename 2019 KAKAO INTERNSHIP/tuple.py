def solution(s):
    raw = [];
    count = [0] * 100001;
    temp = [];
    answer = []
    num = '';
    for i in s :
        if i == '{' or i == '}' or i == ',' :
            if len(num) > 0 :
                raw.append(num);
            num = '';
        else :
            num += i;
    for num in raw :
        count[int(num)] += 1;
    for i in range(len(count)) :
        temp.append((count[i], i));
    temp.sort(reverse = True);
    for t in temp :
        cnt, num = t;
        if cnt == 0 :
            break;
        else :
            answer.append(num);
    return answer