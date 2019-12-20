#!/usr/bin/env python3
from operator import itemgetter


class Line:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.length = 0
        self.positions = [(0, 0)]

    def update(self, val):
        num = int(val[1:])
        if val[0] == 'U':
            for i in range(1, num):
                self.positions.append((self.x, self.y + i))
            self.y += num
        elif val[0] == 'D':
            for i in range(1, num):
                self.positions.append((self.x, self.y - i))
            self.y -= num
        elif val[0] == 'R':
            for i in range(1, num):
                self.positions.append((self.x + i, self.y))
            self.x += num
        elif val[0] == 'L':
            for i in range(1, num):
                self.positions.append((self.x - i, self.y))
            self.x -= num

        self.positions.append((self.x, self.y))
        self.length += num

    def get_pos_length(self, val):
        place = self.positions.index(val)
        return len(self.positions[:place])

    def __len__(self):
        return self.length


def manhattan_distance(val):
    return abs(0-val[0]) + abs(0-val[1])


def main():
    with open('input.txt') as fp:
        data = [list(d.strip().split(',')) for d in fp.readlines()]

    lines = []
    for idx, d in enumerate(data):
        l = Line(name=idx)
        for val in d:
            l.update(val)
        lines.append(l)

    line0 = lines[0]
    line1 = lines[1]

    new_lengths = []
    for i in set(line0.positions).intersection(set(line1.positions)):
        length0 = line0.get_pos_length(i)
        length1 = line1.get_pos_length(i)

        m_dist = manhattan_distance(i)
        length = length0 + length1
        if length > 0:
            new_lengths.append((m_dist, length))

    print('shortest manhattan distance: {}'.format(sorted(new_lengths, key=itemgetter(0))[0][0]))
    print('shortest overall intersection: {}'.format(sorted(new_lengths, key=itemgetter(1))[0][1]))

if __name__ == '__main__':
    main()
