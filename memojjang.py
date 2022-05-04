n = int(input());
data = list(map(int, input().split()));
data.sort();
checkIfCanBeMade = 1;

for coin in data :
    if checkIfCanBeMade < coin :
        break;
    checkIfCanBeMade += coin;

print(checkIfCanBeMade);
