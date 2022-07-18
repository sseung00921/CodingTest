n = int(input());
target = n;
cycleCnt = 0;

while True :
    cycleCnt += 1;

    fir = n // 10;
    sec = n % 10;
    sum = fir + sec;
    newN = sec*10 + sum%10;
    if newN == target :
        break;
    n = newN

print(cycleCnt);