def findLenCommonSet(set1, set2) :
    lenCommonSet = 0;
    realSet1 = set(set1);
    realSet2 = set(set2);
    commonSet = realSet1 & realSet2;
    for e in commonSet :
        repeatedCnt = min(set1.count(e), set2.count(e));
        lenCommonSet += repeatedCnt;
    return lenCommonSet;

def makeMultipleSet(str) :
    rtnList = [];
    for i in range(len(str) - 1) :
        subStr = str[i : i + 2];
        if subStr[0].isalpha() and subStr[1].isalpha() :
            subStr = subStr.lower();
            rtnList.append(subStr);
    return rtnList;


def solution(str1, str2):
    answer = 0
    set1 = makeMultipleSet(str1);
    set2 = makeMultipleSet(str2);
    print(set1, set2)
    lenCommonSet = findLenCommonSet(set1, set2);
    lenSet1 = len(set1);
    lenSet2 = len(set2);
    print(lenCommonSet, lenSet1, lenSet2);
    if lenSet1 == 0 and lenSet2 == 0 :
        return 1*65536;
    answer = int((lenCommonSet / (lenSet1 + lenSet2 - lenCommonSet)) * 65536);
    return answer

str1 = "FRANCE";
str2 = "french";
print(solution(str1, str2));

str1 = "aa1+aa2";
str2 = "AAAA12";
print(solution(str1, str2));