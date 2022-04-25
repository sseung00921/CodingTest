from itertools import combinations;

def solution(relation):
    rowNum = len(relation);
    colNum = len(relation[0]);

    possibleColumnSetList = [];
    for i in range(1, colNum + 1) :
        for possibleColumns in list(combinations(range(colNum), i)) :
            possibleColumnSetList.append(set(possibleColumns));

    hubokeyList = [];

    for possibleColumnSet in possibleColumnSetList :
        tupleArr = [tuple([student[i] for i in possibleColumnSet]) for student in relation];
        if len(set(tupleArr)) != rowNum :
            #in this case, unique is False.
            continue;
        if len(possibleColumnSet) == 1 :
            hubokeyList.append(possibleColumnSet);
        else :
            minimum = True;
            for existingColumnSet in hubokeyList :
                if existingColumnSet.issubset(possibleColumnSet) :
                    minimum = False;
                    break;
            if minimum == True :
                hubokeyList.append(possibleColumnSet);
    return len(hubokeyList);

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]];
print(solution(relation));