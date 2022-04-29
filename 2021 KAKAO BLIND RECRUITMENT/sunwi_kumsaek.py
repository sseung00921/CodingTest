from bisect import bisect_left;

dic = {
    "-" : 0, "cpp" : 1, "java" : 2, "python" : 3,
    "backend" : 1, "frontend" : 2,
    "junior" : 1, "senior" : 2,
    "chicken" : 1, "pizza" : 2
}

def solution(info, query): #2022-04-29
    graph = [[] for _ in range(4*3*3*3)];
    answer = []
    for human in info :
        data = human.split(' ');
        attrArr = [dic[data[0]]*(3*3*3), dic[data[1]]*(3*3), dic[data[2]]*3, dic[data[3]]];
        score = int(data[4]);

        for i in range(1 << 4) :
            idx = 0;
            for j in range(4) : #4 is len(attrArr)
                if i & (1 << j) :
                    idx += attrArr[j];
            graph[idx].append((score));

    for i in range(4*3*3*3) :
        graph[i].sort();

    for req in query :
        reqData = req.split(' ');
        idx = dic[reqData[0]]*(3*3*3) + dic[reqData[2]]*(3*3) + dic[reqData[4]]*3 + dic[reqData[6]];
        bisect_left_idx = bisect_left(graph[idx], int(reqData[7]));
        cntOfRequstedPeople = len(graph[idx]) - bisect_left_idx;
        answer.append(cntOfRequstedPeople);
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"];
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"];
print(solution(info, query));