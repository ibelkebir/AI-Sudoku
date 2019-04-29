#!/usr/bin/python3
import sys
import time

class pos:
    def __init__(self, index, vals):
        self.index = index
        self.vals = vals

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class Dlist:
    def __init__(self):
        self.first = None
        self.last = None
    def insert(self, value):
        if self.first == None:
            self.first = Node(value)
            self.last = self.first
            return
        cur = self.first
        if len(cur.value.vals) > len(value.vals):
            cur.previous = Node(value)
            self.first = cur.previous
            cur.previous.next = cur
            if self.last == None:
                self.last = cur
            return
        if cur.next == None:
            self.last = Node(value)
            cur.next = self.last
            self.last.previous = cur
            return
        while len(cur.value.vals) <= len(value.vals) and cur.next != None:
            cur = cur.next
        temp = Node(value)
        if cur.next == None and len(cur.value.vals) < len(value.vals):
            cur.next = temp
            temp.previous = cur
            self.last = temp
            return
        cur.previous.next = temp
        temp.previous = cur.previous
        temp.next = cur
        cur.previous = temp

f = open(sys.argv[1],'r')
input = f.read().split('\n')
input = [x.split(',') for x in input]
board = []
i = 0
name = sys.argv[3].split(',')
while i < len(input):
    if len(input[i]) > 1 and input[i][1] == name[1]:
        board = input[i+1:i+10]
        break
    i += 1
board = [j for i in board for j in i]

cliques=[
    [0,1,2,3,4,5,6,7,8],
    [9,10,11,12,13,14,15,16,17],
    [18,19,20,21,22,23,24,25,26],
    [27,28,29,30,31,32,33,34,35],
    [36,37,38,39,40,41,42,43,44],
    [45,46,47,48,49,50,51,52,53],
    [54,55,56,57,58,59,60,61,62],
    [63,64,65,66,67,68,69,70,71],
    [72,73,74,75,76,77,78,79,80],
    [0,9,18,27,36,45,54,63,72],
    [1,10,19,28,37,46,55,64,73],
    [2,11,20,29,38,47,56,65,74],
    [3,12,21,30,39,48,57,66,75],
    [4,13,22,31,40,49,58,67,76],
    [5,14,23,32,41,50,59,68,77],
    [6,15,24,33,42,51,60,69,78],
    [7,16,25,34,43,52,61,70,79],
    [8,17,26,35,44,53,62,71,80],
    [0,1,2,9,10,11,18,19,20],
    [3,4,5,12,13,14,21,22,23],
    [6,7,8,15,16,17,24,25,26],
    [27,28,29,36,37,38,45,46,47],
    [30,31,32,39,40,41,48,49,50],
    [33,34,35,42,43,44,51,52,53],
    [54,55,56,63,64,65,72,73,74],
    [57,58,59,66,67,68,75,76,77],
    [60,61,62,69,70,71,78,79,80]
]
cd = {}

for i in range(81):
    for clique in cliques:
        if i in clique:
            if i not in cd:
                cd[i] = []
                cd[i].extend(clique)
                cd[i].remove(i)
            else:
                cd[i].extend(clique)
                cd[i].remove(i)

spots = Dlist()
for i in range(len(board)):
    if board[i] == "_":
        p = pos(i, [])
        for j in range(1,10):
            can_move = True
            for k in cd[i]:
                if board[k] == str(j):
                        can_move = False
            if can_move:
                p.vals.append(j)
        spots.insert(p)

def to_board():
    p = []
    p.append(board[0])
    for i in range(1,81):
        p.append(board[i])
        if len(p) == 9:
            print(','.join(p))
            p = []
    print('\n')

b = [0]
def solve(i):
    print(i.value.index)
    to_board()
    time.sleep(.3)
    for j in i.value.vals:
        print(j)
        can_move = True
        for k in cd[i.value.index]:
            if board[k] == str(j):
                can_move = False
        if can_move:
            board[i.value.index] = str(j)
            forced_vals = [j]
            def force(val, cur):
                t = i
                while t.next != None:
                    t = t.next
                    if t.value.index in cd[cur.value.index]:
                        removed = False
                        if val in t.value.vals:
                            t.value.vals.remove(val)
                            removed = True
                        if len(t.value.vals) == 1 and removed:
                            force(t.value.vals[0], t)
                if t.value.index in cd[cur.value.index]:
                    removed = False
                    if val in t.value.vals:
                        t.value.vals.remove(val)
                        removed = True
                    if len(t.value.vals) == 1 and removed:
                        forced_vals.append(t.value.vals[0])
                        force(t.value.vals[0], t)
            force(j, i)
            forced = False
            t = i.next
            while t != None:
                if len(t.value.vals) == 0:
                    forced = True
                t = t.next
            if not forced and (i.next == None or solve(i.next)):
                return True
            t = i.next
            board[i.value.index] = "_"
            while t != None:
                for val in forced_vals:
                    can_move = True
                    for k in cd[t.value.index]:
                        if board[k] == str(val):
                            can_move = False
                    if can_move:
                        t.value.vals.append(j)
                    t = t.next
    b[0] += 1
    board[i.value.index] = "_"
    return False

solve(spots.first)
#print(b[0])
f = open(sys.argv[2], 'w+')
i = 9
while i <= 81:
    f.write(','.join(board[i-9:i]) + '\n')
    i += 9
f.close()
