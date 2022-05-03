s = input();

zeroCnt = 0;
oneCnt = 0;

for i in range(1, len(s)) :
    if s[i - 1] == s[i] :
        continue;
    else :
        if s[i - 1] == '0' :
            zeroCnt += 1;
        else :
            oneCnt += 1;

if s[-1] == '0' :
    zeroCnt += 1;
else :
    oneCnt += 1;

print(min(zeroCnt, oneCnt));
