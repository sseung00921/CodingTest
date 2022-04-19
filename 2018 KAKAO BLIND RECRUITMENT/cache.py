from collections import deque;

def manageCache(cache, cacheSize, city) :
    if cacheSize == 0 :
        return;
    if len(cache) < cacheSize :
        cache.append(city)
        return;
    else :
        if city in cache :
            cache.remove(city);
            cache.append(city);
            return;
        else :
            cache.popleft();
            cache.append(city);
            return;

def solution(cacheSize, cities):
    cache = deque([]);
    answer = 0
    for city in cities :
        city = city.lower();
        if city in cache :
            answer += 1;
        else :
            answer += 5;
        manageCache(cache, cacheSize, city);
    return answer

cacheSize = 3;
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities));

cacheSize = 3;
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize, cities));