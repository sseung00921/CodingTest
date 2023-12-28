def getLongTime(hh, mm, ss) :
    return int(hh)*3600 + int(mm)*60 + int(ss);

def getStrTime(longTime) :
    hh = longTime // 3600;
    longTime -= hh*3600;
    mm = longTime // 60;
    ss = longTime % 60;
    return hh, mm, ss;

def getHourPos(hh, mm, ss) :
    if hh >= 12 :
        hh -= 12;
    rtnVal = hh * 5 + mm * (1/12) + ss * (1/720);
    return rtnVal;

def getMiniPos(mm, ss) :
    rtnVal = mm + ss * (1/60);
    return rtnVal;

def calc(startTime, endTime) :
    rtnCnt = 0;
    for time in range(startTime, endTime + 1) :
        if time == 0 or time == 43200 :
            rtnCnt += 1;
            continue;
        nowHour, nowMini, nowSec = getStrTime(time);
        nextHour, nextMini, nextSec = getStrTime(time + 1);
        nowHourPos = getHourPos(nowHour, nowMini, nowSec);
        nowMiniPos = getMiniPos(nowMini, nowSec);
        nowSecPos = nowSec;

        nextHourPos = getHourPos(nextHour, nextMini, nextSec);
        nextMiniPos = getMiniPos(nextMini, nextSec);
        nextSecPos = nextSec;
        if nextSecPos == 0 :
            nextSecPos = 60;
        if nextMiniPos == 0 :
            nextMiniPos = 60;
        if nextHourPos == 0 :
            nextHourPos = 60;
        if nextSecPos == 60 and nextMiniPos == 60 and nextHourPos == 60 :
            continue;
        if nowMiniPos == nowSecPos :
            rtnCnt += 1;
        elif time != endTime and nowMiniPos > nowSecPos and nextMiniPos < nextSecPos :
            rtnCnt += 1;
        if nowHourPos == nowSecPos :
            rtnCnt += 1;
        elif time != endTime and nowHourPos > nowSecPos and nextHourPos < nextSecPos :
            rtnCnt += 1;
    return rtnCnt;

def solution(h1, m1, s1, h2, m2, s2):
    startTime = getLongTime(h1, m1, s1);
    endTime = getLongTime(h2, m2, s2);
    return calc(startTime, endTime);

print(solution(2, 59, 0, 3, 1, 0));