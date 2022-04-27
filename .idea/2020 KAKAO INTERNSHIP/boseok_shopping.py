def solution(gems):
    cntMapper = {gems[0] : 1}
    lenKind = len(set(gems));
    lenGems = len(gems);

    answer = [0, 1000001]
    countedKind = 1;
    start = 0; end = 0;
    while True :
        if countedKind < lenKind :
            end += 1;
            if end == lenGems :
                break;
            if cntMapper.get(gems[end], 0) == 0 :
                cntMapper[gems[end]] = 1;
                countedKind += 1;
            else :
                cntMapper[gems[end]] += 1;
        else :
            if end - start < answer[1] - answer[0] :
                answer[0] = start + 1;
                answer[1] = end + 1;
            cntMapper[gems[start]] -= 1;
            if cntMapper.get(gems[start]) == 0 :
                countedKind -= 1;
            start += 1;
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"];
print(solution(gems));