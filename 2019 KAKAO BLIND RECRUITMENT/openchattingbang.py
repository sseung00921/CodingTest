ussrIdNicknameMapper = dict();

def solution(record):
    answer = []

    for userInfo in record :
        splittedUserInfo = userInfo.split(' ');
        if splittedUserInfo[0] == "Leave" :
            continue;
        else:
            ussrIdNicknameMapper[splittedUserInfo[1]] = splittedUserInfo[2];

    for userInfo in record :
        splittedUserInfo = userInfo.split(' ');
        if splittedUserInfo[0] == "Enter" :
            answer.append(ussrIdNicknameMapper[splittedUserInfo[1]] + "님이 들어왔습니다.")
        elif splittedUserInfo[0] == "Leave" :
            answer.append(ussrIdNicknameMapper[splittedUserInfo[1]] + "님이 나갔습니다.")
        else :
            continue;

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"];
print(solution(record));