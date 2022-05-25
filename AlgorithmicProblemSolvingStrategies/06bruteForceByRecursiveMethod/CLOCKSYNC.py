INF = 1000;
SWITCHES = 10;
CLOCKS = 16;
LINKED_STATUS = [
    [0,1,2], #0번 스위치가 0,1,2의 시계에 연결
    [3,7,9,11],
    [4,10,14,15],
    [0,4,5,6,7],
    [6,7,8,10,12],
    [0,2,14,15],
    [3,14,15],
    [4,5,7,14,15],
    [1,2,3,4,5],
    [3,4,5,9,13]
]

def checkIfAllSeeing12(clockStatus) :
    for i in range(CLOCKS) :
        if clockStatus[i] != 12 :
            return False;
    return True;

def push(clockStatus, switchNum) :
    for clockNum in LINKED_STATUS[switchNum] :
        clockStatus[clockNum] += 3;
        if clockStatus[clockNum] == 15 :
            clockStatus[clockNum] = 3;

def dfs(clockStatus, pushedSwitchCnt) :
    if pushedSwitchCnt == SWITCHES :
        return 0 if checkIfAllSeeing12(clockStatus) == True else INF;

    rtn = INF;
    for repeatedCnt in range(4) :
        rtn = min(rtn, repeatedCnt + dfs(clockStatus, pushedSwitchCnt + 1));
        push(clockStatus, pushedSwitchCnt);
    return rtn;

tc = int(input());
while tc > 0 :
    clockStatus = list(map(int, input().split()));
    print(-1 if dfs(clockStatus, 0) > 500 else dfs(clockStatus, 0));
    tc -= 1;