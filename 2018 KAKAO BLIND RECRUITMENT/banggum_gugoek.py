def transForm(akbo) :
    akbo = akbo.replace("C#", "c");
    akbo = akbo.replace("D#", "d");
    akbo = akbo.replace("F#", "f");
    akbo = akbo.replace("G#", "g");
    akbo = akbo.replace("A#", "a");
    return akbo;

def toMini(strTime) :
    times = strTime.split(":");
    hour = int(times[0]);
    mini = int(times[1]);
    return hour*60 + mini;

def toPlayedMelody(givenMelody, duration) :
    lenGivenMelody = len(givenMelody);
    playedMelody = '';

    repeatedTime = duration // lenGivenMelody;
    cuttingPoint = duration % lenGivenMelody;

    for _ in range(repeatedTime) :
        playedMelody += givenMelody;
    playedMelody += givenMelody[ : cuttingPoint];

    return playedMelody;

def match(seekingMelody, givenMelody) :
    if seekingMelody in givenMelody :
        return True;
    return False;

def solution(m, musicinfos):
    m = transForm(m);
    hubo = [];
    answer = ''
    idx = 0;
    for musicinfo in musicinfos :
        idx += 1;
        data = musicinfo.split(",");
        start, end, name, givenMelody = data;
        givenMelody = transForm(givenMelody);
        duration = toMini(end) - toMini(start);
        playedMelody = toPlayedMelody(givenMelody, duration);
        if match(m, playedMelody) == True :
            hubo.append((duration, idx, name));

    if len(hubo) == 0 :
        return "(None)"

    hubo.sort(key = lambda x : (-int(x[0]), int(x[1])));
    answer = hubo[0][2];
    return answer

m = "CC#BCC#BCC#BCC#B";
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"];
print(solution(m, musicinfos));