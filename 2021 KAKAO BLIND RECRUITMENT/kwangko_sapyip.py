def translateStrTime(strTime) :
    h, m, s = strTime.split(":");
    return int(h)*60*60 + int(m)*60 + int(s);

def solution(play_time, adv_time, logs):
    play_time = translateStrTime(play_time);
    adv_time = translateStrTime(adv_time);
    d = [0] * (play_time + 1);
    for log in logs :
        sLog, eLog = log.split("-");
        sLog = translateStrTime(sLog);
        eLog = translateStrTime(eLog);
        d[sLog] += 1;
        d[eLog] -= 1;

    for i in range(1, play_time + 1) :
        d[i] = d[i] + d[i - 1];

    maxStartIdx = 0;
    maxDuration = sum(d[:adv_time]);
    searchingDuration = sum(d[:adv_time]);
    for i in range(adv_time, play_time + 1) :
        searchingDuration -= d[i - adv_time];
        searchingDuration += d[i];
        if searchingDuration > maxDuration :
            maxDuration = searchingDuration;
            maxStartIdx = i - adv_time + 1;

    return "%02d:%02d:%02d" % (maxStartIdx//3600, maxStartIdx//60%60, maxStartIdx%60);

play_time = "02:03:55";
adv_time = "00:14:15";
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"];
print(solution(play_time, adv_time, logs));