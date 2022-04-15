import copy;
lenBanned_id = 0;

def checkIfPossible(bannedId, userId) :
    n = len(userId);
    if len(bannedId) != n :
        return False;
    else :
        for i in range(n) :
            if bannedId[i] == '*' :
                continue;
            elif bannedId[i] == userId[i] :
                continue;
            else :
                return False;
    return True;

possibleArr = [];
def dfs(user_id, banned_id, arr, level) :
    if level == lenBanned_id :
        arr.sort();
        if arr not in possibleArr :
            possibleArr.append(arr);
        return;
    bId = banned_id[level];
    for uId in user_id :
        if checkIfPossible(bId, uId) :
            tUser_id = copy.deepcopy(user_id);
            tUser_id.remove(uId);
            tArr = copy.deepcopy(arr);
            tArr.append(uId);
            dfs(tUser_id, banned_id, tArr, level + 1);



def solution(user_id, banned_id):
    answer = 0;
    global lenBanned_id;
    lenBanned_id = len(banned_id);
    dfs(user_id, banned_id, [], 0);
    answer = len(possibleArr);
    return answer;