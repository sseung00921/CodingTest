import sys;
sys.setrecursionlimit(10000000);

def dicideRoomNum(lastNumMap, req) :
    if req not in lastNumMap :
        lastNumMap[req] = req + 1;
        return req;
    lastNumMap[req] = dicideRoomNum(lastNumMap, lastNumMap[req]);
    return lastNumMap[req];


def solution(k, room_number):
    lastNumMap = dict();
    answer = []
    for req in room_number :
        assigned = dicideRoomNum(lastNumMap, req);
        answer.append(assigned);
    return answer

k = 10;
room_mumber = [1,3,4,1,3,1];
print(solution(k, room_mumber));