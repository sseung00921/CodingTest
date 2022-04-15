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
    arr = copy.deepcopy(arr);
    if level == lenBanned_id :
        arr.sort();
        if arr not in possibleArr :
            possibleArr.append(arr);
        return;
    bId = banned_id[level];
    tUser_id = copy.deepcopy(user_id);
    for uId in user_id :
        if checkIfPossible(bId, uId) :
            tUser_id.remove(uId);
            arr.append(uId);
            dfs(tUser_id, banned_id, arr, level + 1);
            arr.pop();
            tUser_id.append(uId);



def solution(user_id, banned_id):
    answer = 0;
    global lenBanned_id;
    lenBanned_id = len(banned_id);
    dfs(user_id, banned_id, [], 0);
    answer = len(possibleArr);
    return answer;