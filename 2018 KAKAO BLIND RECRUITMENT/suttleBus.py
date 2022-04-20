import heapq;

def transToMini(strTime) :
    times = strTime.split(":");
    hour = int(times[0]);
    mini = int(times[1]);
    return hour * 60 + mini;

def transToStr(miniTime) :
    hour = str(miniTime // 60);
    mini = str(miniTime % 60);
    if len(hour) == 1 :
        hour = "0" + hour;
    if len(mini) == 1 :
        mini = "0" + mini;
    return hour + ":" + mini;

def solution(n, t, m, timetable):
    lastBusTime = (n - 1)*t + 540;
    miniVerTimetable = [];
    for time in timetable :
        miniVerTimetable.append(transToMini(time));

    miniVerTimetable.sort();

    busArrivedTime = 540;
    for i in range(n - 1) :
        onBoard = 0;
        while onBoard < m :
            if len(miniVerTimetable) == 0 :
                return transToStr(lastBusTime);
            crewArrivedTime = heapq.heappop(miniVerTimetable);
            if crewArrivedTime > busArrivedTime :
                heapq.heappush(miniVerTimetable, crewArrivedTime);
                break;
            onBoard += 1;
        busArrivedTime += t;

    lastBusOnBoard = 0;
    while lastBusOnBoard < m - 1 :
        if len(miniVerTimetable) == 0 :
            return transToStr(lastBusTime);
        crewArrivedTime = heapq.heappop(miniVerTimetable);
        if crewArrivedTime > busArrivedTime :
            heapq.heappush(miniVerTimetable, crewArrivedTime);
            return transToStr(lastBusTime);
        lastBusOnBoard += 1;

    if len(miniVerTimetable) == 0 :
        return transToStr(lastBusTime);
    lastPersonToTakeBusArrivedTime = heapq.heappop((miniVerTimetable));
    if lastPersonToTakeBusArrivedTime > busArrivedTime :
        return transToStr(lastBusTime);
    else :
        return transToStr(lastPersonToTakeBusArrivedTime - 1);

n = 2;
t = 10;
m = 2;
timetable = ["09:10", "09:09", "08:00"];
print(solution(n, t, m, timetable));