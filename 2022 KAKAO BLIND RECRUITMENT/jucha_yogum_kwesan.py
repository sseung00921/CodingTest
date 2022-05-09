import math;

carInTimeMapper = dict();
carDurationMapper = dict();

def convert(strTime) :
    hh, mm = strTime.split(":");
    return int(hh) * 60 + int(mm);

def solution(fees, records):
    baseTime = fees[0]; baseFee = fees[1]; danwiTime = fees[2]; danwiFee = fees[3];
    for r in records :
        time, carNum, inOut = r.split();
        if inOut == "IN" :
            carInTimeMapper[carNum] = convert(time);
            if carNum not in carDurationMapper :
                carDurationMapper[carNum] = 0;
        else :
            carDurationMapper[carNum] += convert(time) - carInTimeMapper[carNum];
            del carInTimeMapper[carNum];

    lastOutTime = convert("23:59");
    for carNum, inTime in carInTimeMapper.items() :
        carDurationMapper[carNum] += lastOutTime - inTime;

    answer = []
    for carNum, duration in sorted(carDurationMapper.items()) :
        if duration < baseTime :
            answer.append(baseFee);
        else :
            answer.append(baseFee + (math.ceil(int((duration - baseTime))/danwiTime))*danwiFee);
    return answer

fees = [180, 5000, 10, 600];
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"];
print(solution(fees, records));