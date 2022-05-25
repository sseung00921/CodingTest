def karat(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        l = max(len(str(x)),len(str(y)))
        hl = l // 2

        a = x // 10**(hl)
        b = x % 10**(hl)
        c = y // 10**(hl)
        d = y % 10**(hl)

        z0 = karat(b,d)
        z1 = karat((a+b),(c+d))
        z2 = karat(a,c)

        return (z2 * 10**(2*hl)) + ((z1 - z2 - z0) * 10**(hl)) + (z0);

print(karat(111000, 111000));
print(karat(155,199));

#이하는 그냥 평범한 배열단위의 곱셈 관련 로직인데 그냥 참고로 적어둠.

def normalize(numArr) :
    numArr.append(0);
    for i in range(len(numArr) - 1) :
        if numArr[i] < 0 :
            borrow = (abs(numArr[i]) + 9) / 10;
            numArr[i + 1] -= borrow;
            numArr[i] += (borrow*10);
        else :
            numArr[i + 1] += (numArr[i] // 10);
            numArr[i] %= 10;
    while len(numArr) > 1 and numArr[-1] == 0 :
        numArr.pop();

def multiply(a, b) :
    c = [0] * (len(a) + len(b) + 1);
    for i in range(len(a)) :
        for j in range(len(b)) :
            c[i + j] += (a[i] * b[j]);
    normalize(c);
    return c;