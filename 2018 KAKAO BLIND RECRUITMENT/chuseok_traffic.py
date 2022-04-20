def getMillTime(str) :
    times = str.split(":");
    if len(times) == 1 :
        return int(float(times[0])*1000);
    else :
        hour = int(times[0]);
        mini = int(times[1]);
        sec = float(times[2]);
        return hour*3600000 + mini*60000 + int(sec*1000);

def solution(lines):
    startPoints = [];
    endPoints = [];
    tasks =[];

    for line in lines :
        times = line.split(" ");
        endTime = times[1];
        duration = times[2][:-1];

        endMillTime = getMillTime(endTime);
        startMillTime = getMillTime(endTime) - getMillTime(duration) + 1;

        startPoints.append(startMillTime);
        endPoints.append(endMillTime);
        tasks.append((startMillTime, endMillTime));

    answer = 0
    for endPoint in endPoints :
        cnt = 0;
        for task in tasks :
            start, end = task;
            if end >= endPoint and start <= endPoint+ 999 :
                cnt += 1;
        answer = max(cnt, answer);

    return answer


lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
];
print(solution(lines));