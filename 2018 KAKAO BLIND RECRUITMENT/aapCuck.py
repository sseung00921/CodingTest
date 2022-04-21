def findKeywordLen(mapper, str) :
    keywordLen = len(str);
    while True :
        subStr = str[ : keywordLen];
        if subStr in mapper :
            return keywordLen;
        keywordLen -= 1;
    return idx;

def solution(msg):
    mapper = dict();
    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    mapperIdx = 1

    for c in str :
        mapper[c] = mapperIdx;
        mapperIdx += 1;

    answer = []
    while len(msg) > 0 :
        keywordLen = findKeywordLen(mapper, msg);
        keyword = msg[0 : keywordLen];
        answer.append(mapper[keyword]);
        newKeywordToAdd = msg[0 : keywordLen + 1];
        mapper[newKeywordToAdd] = mapperIdx;
        mapperIdx += 1;
        msg = msg[keywordLen : ];

    return answer


msg = "TOBEORNOTTOBEORTOBEORNOT";
print(solution(msg));