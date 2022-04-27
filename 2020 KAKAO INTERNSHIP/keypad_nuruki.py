nowRightPos = 11;
nowLeftPos = 9;

def solution(numbers, hand):
    global nowRightPos;
    global nowLeftPos;
    answer = ''
    for number in numbers :
        if number == 1 or number == 4 or number == 7 :
            answer += "L";
            nowLeftPos = number - 1;
            continue;
        elif number == 3 or number == 6 or number == 9 :
            answer += "R"
            nowRightPos = number - 1;
            continue;
        else :
            if number == 0 :
                number = 10;
            else :
                number -= 1;
            r = number // 3;
            c = number % 3;
            dLeft = abs(nowLeftPos//3 - r) + abs(nowLeftPos%3 - c);
            dRight = abs(nowRightPos//3 - r) + abs(nowRightPos%3 - c);
            if dLeft < dRight :
                answer += "L";
                nowLeftPos = number;
                continue;
            elif dRight < dLeft :
                answer += "R";
                nowRightPos = number;
                continue;
            elif dLeft == dRight :
                if hand == "right" :
                    answer += "R";
                    nowRightPos = number;
                else :
                    answer += "L";
                    nowLeftPos = number;
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
hand = "right";
print(solution(numbers, hand));