from itertools import combinations;
combiCntDic = dict();

def solution(orders, course):
    answer = [];
    for order in orders :
        for i in course :
            for combi in list(combinations(order, i)) :
                combi = sorted(combi);
                key = ''.join(combi);
                if key not in combiCntDic :
                    combiCntDic[key] = 1;
                else :
                    combiCntDic[key] += 1;

    for i in course :
        maxCnt = 0;
        for key in combiCntDic.keys() :
            if len(key) == i :
                maxCnt = max(maxCnt, combiCntDic[key]);
        for key in combiCntDic.keys() :
            if len(key) == i :
                if combiCntDic[key] == maxCnt and combiCntDic[key] >= 2 :
                    answer.append(key);
    answer.sort();
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"];
course = [2,3,4];
print(solution(orders, course));
