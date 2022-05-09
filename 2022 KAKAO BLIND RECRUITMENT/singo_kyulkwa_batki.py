cmdSet = set();
singoCntDic = {};
stopIdSet = set();
wongoPigoMapper = {};

def solution(id_list, report, k) :
    answer = []
    for r in report :
        if r in cmdSet :
            continue;
        cmdSet.add(r);
        wongo, pigo = r.split(' ');
        if pigo not in singoCntDic :
            singoCntDic[pigo] = 1;
        else :
            singoCntDic[pigo] += 1;
        if wongo not in wongoPigoMapper :
            wongoPigoMapper[wongo] = [pigo];
        else :
            wongoPigoMapper[wongo].append(pigo);

    for id, singoCnt in singoCntDic.items() :
        if singoCnt >= k :
            stopIdSet.add(id);

    for i in range(len(id_list)) :
        if id_list[i] not in wongoPigoMapper :
            answer.append(0);
        else :
            getMailCnt = 0;
            for pigo in wongoPigoMapper[id_list[i]] :
                if pigo in stopIdSet :
                    getMailCnt += 1;
            answer.append(getMailCnt);

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"];
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"];
k = 2;
print(solution(id_list, report, k));