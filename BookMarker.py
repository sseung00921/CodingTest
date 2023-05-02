Arr = [];
Summ = 0;
PrevSum = 0;

def parser(strHour) :
    temp = strHour.split(":");
    if len(temp) >= 3 :
        hh, mm, ss = strHour.split(":");
        if int(ss) == 0 :
            mm = int(mm);
        elif int(ss) > 0 :
            mm = int(mm) + 1;
        return int(hh)*60 + mm;
    else :
        mm, ss= strHour.split(":");
        if int(ss) == 0 :
            mm = int(mm);
        elif int(ss) > 0 :
            mm = int(mm) + 1;
        return mm;

def calculate(targetMin) :
    global Summ;
    global PrevSum;
    for i in range(len(Arr)) :
        Summ += parser(Arr[i]);
        if Summ < targetMin :
            PrevSum = Summ;
        elif Summ >= targetMin :
            return Arr[-1], targetMin - PrevSum;
    return None, None;

def bookMark(targetMin) :
    global Summ;
    global PrevSum;
    while True :
        Summ = 0;
        PrevSum = 0;
        strHour = input();
        Arr.append(strHour);
        lastInput, miniute = calculate(targetMin);
        if Summ >= targetMin :
            print(lastInput, miniute);
            break;

targetMin = int(input());
bookMark(targetMin);