def solution(replies, n, k):
    answer = []
    for reply in replies :
        check = True;
        lenWord = n;
        while lenWord <= len(reply):
            idx = 0;
            while idx + lenWord <= len(reply) :
                repeated = 1;
                cut = reply[idx : idx + lenWord];
                #print(cut);
                for i in range(idx + lenWord, len(reply), lenWord) :
                    if i + lenWord > len(reply) :
                        break;
                    #print(reply[i : i + lenWord] + 'a');
                    if reply[i : i + lenWord] == reply[i - lenWord : i] :
                        repeated += 1;
                if repeated >= k :
                    check = False;
                    break;
                idx += 1;
            if check == False :
                break;
            lenWord += 1;
        if check == False :
            answer.append(0);
        else :
            answer.append(1);
    return answer

replies = ["FCBBBFCBBECBB"];
n = 3;
k = 2;
print(solution(replies, n, k));