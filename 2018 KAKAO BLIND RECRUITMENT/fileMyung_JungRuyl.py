def spliter(fileName) :
    head = '';
    number = '';
    tail = '';

    splitPoint1 = 0;
    splitPoint2 = 0;

    for i in range(len(fileName)) :
        if fileName[i].isnumeric() :
            splitPoint1 = i;
            break;

    cnt = 0;
    for i in range(splitPoint1, len(fileName)) :
        if not fileName[i].isnumeric() or cnt >= 5 :
            splitPoint2 = i;
            break;
        elif i == len(fileName) - 1 :
            splitPoint2 = len(fileName)
        cnt += 1;

    head = fileName[0 : splitPoint1];
    number = fileName[splitPoint1 : splitPoint2];
    tail = fileName[splitPoint2 : ]

    return head, number, tail;

def solution(files):
    arrayForSort = [];
    answer = []

    idx = 0;
    for fileName in files :
        head, number, tail = spliter(fileName);
        arrayForSort.append((head.lower(), int(number), idx));
        idx += 1;

    arrayForSort.sort();

    for file in arrayForSort :
        idx = file[2];
        answer.append(files[idx]);
    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"];
print(solution(files))