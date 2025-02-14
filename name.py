
import string

firsts = set()
lasts = {}

with open('first.txt') as f:
    for line in f.readlines():
        name = line.split()[0]
        firsts.add(name)

with open('last.txt') as f:
    for line in f.readlines():
        name = line.split()[0]
        sort = ''.join(sorted(name))
        if sort not in lasts:
            lasts[sort] = []
        lasts[sort].append(name)


def get_name(base):
    want = []
    for char in base:
        if char in string.ascii_letters:
            want.append(char.upper()) 

    for first in firsts:
        res = {}
        for i in want:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        for c in first:
            if c in res:
                if res[c] == 1:
                    del res[c]
                else:
                    res[c] -= 1
            else:
                break
        else:
            rest = ''
            for i in res:
                rest += i * res[i]
            rest = ''.join(sorted(rest))
            if rest in lasts:
                last = lasts[rest][0]
                return first[0] + first[1:].lower() + ' ' + last[0] + last[1:].lower()

while True:
    name = input()
    out = get_name(name)
    print(out)
