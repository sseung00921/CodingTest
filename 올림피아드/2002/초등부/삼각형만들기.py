import sys;
input = sys.stdin.readline;

n = int(input());
possibles = [];
for i in range(1, n) :
    smallsSum, largest = i, n - i;
    if smallsSum <= largest :
        continue;
    possibles.append((smallsSum, largest));

answer = 0;
for possible in possibles :
    smallsSum, largest = possible
    if (smallsSum + 1) // 2 > largest :
        continue;
    answer += (largest - (smallsSum + 1) // 2 + 1);
print(answer);