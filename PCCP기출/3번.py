def getNumTime(hh, mm, ss) :
    return int(hh)*3600 + int(mm)*60 + int(ss);

def getStrTime(numTime) :
    hh = numTime // 3600;
    numTime -= hh*3600;
    mm, ss = numTime // 60, numTime % 60;
    return hh, mm, ss;

def getHourPos(hh, mm, ss) :
    if hh >= 12 :
        hh -= 12;
    return hh*5 + mm*(1/12) + ss*(1/720);

def getMiniPos(mm, ss) :
    return mm + ss*(1/60);

def solution(h1, m1, s1, h2, m2, s2):
    startTime = getNumTime(h1, m1, s1);
    endTIme = getNumTime(h2, m2, s2);
    answer = 0;
    for time in range(startTime, endTIme + 1) :
        nowHour, nowMini, nowSec = getStrTime(time);
        nextHour, nextMini, nextSec = getStrTime(time + 1);
        nowHourPos, nowMiniPos, nowSecPos = getHourPos(nowHour, nowMini, nowSec), getMiniPos(nowMini, nowSec), nowSec;
        nextHourPos, nextMiniPos, nextSecPos = getHourPos(nextHour, nextMini, nextSec), getMiniPos(nextMini, nextSec), nextSec;

        if nextSecPos == 0 :
            nextSecPos = 60;
        if nextMiniPos == 0 :
            nextMiniPos = 60;
        if nextHourPos == 0 :
            nextHourPos = 60;

        if nowHourPos == nowSecPos :
            answer += 1;
        elif time != endTIme and nowHourPos > nowSecPos and nextHourPos < nextSecPos :
            answer += 1;
        if nowMiniPos == nowSecPos :
            answer += 1;
        elif time != endTIme and nowMiniPos > nowSecPos and nextMiniPos < nextSecPos :
            answer += 1;

    if startTime <= 0 <= endTIme :
        answer -= 1;
    if startTime <= 43200 <= endTIme :
        answer -= 1;

    return answer;