import sys;
from collections import deque;

input = sys.stdin.readline;
K = int(input());
Command = list(input().split());
Start = int(input());
Board = deque([[Start]]);

def undoR() :
    for idx in range(len(Board)) :
        tmp = deque([]);
        for i in Board[idx] :
            if i == 1 :
                tmp.appendleft(0);
            elif i == 0 :
                tmp.appendleft(1);
            elif i == 2 :
                tmp.appendleft(3);
            elif i == 3 :
                tmp.appendleft(2);
        Board[idx] = list(tmp) + list(Board[idx]);


def undoL() :
    for idx in range(len(Board)) :
        tmp = deque([]);
        for i in Board[idx] :
            if i == 1 :
                tmp.appendleft(0);
            elif i == 0 :
                tmp.appendleft(1);
            elif i == 2 :
                tmp.appendleft(3);
            elif i == 3 :
                tmp.appendleft(2);
        Board[idx] = list(Board[idx]) + list(tmp);

def undoD() :
    appendix = deque([]);
    for e in Board :
        tmp = [];
        for i in e :
            if i == 1 :
                tmp.append(3);
            elif i == 3 :
                tmp.append(1);
            elif i == 0 :
                tmp.append(2);
            elif i == 2 :
                tmp.append(0);
        appendix.appendleft(tmp);

    for i in range(len(appendix) - 1, -1, -1) :
        Board.appendleft(appendix[i]);

def undoU() :
    suffix = deque([]);
    for e in Board :
        tmp = [];
        for i in e :
            if i == 1 :
                tmp.append(3);
            elif i == 3 :
                tmp.append(1);
            elif i == 0 :
                tmp.append(2);
            elif i == 2 :
                tmp.append(0);
        suffix.appendleft(tmp);

    for i in range(len(suffix)) :
        Board.append(suffix[i]);

rCommand = Command[::-1];

for cmd in rCommand :
    if cmd == 'R' :
        undoR();
    if cmd == 'L' :
        undoL();
    if cmd == 'D' :
        undoD();
    if cmd == 'U' :
        undoU();

for e in Board :
    print(*e);