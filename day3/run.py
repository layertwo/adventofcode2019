#!/usr/bin/env python3


class Line:
    """
    Line class
    """
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.length = 0
        self._coords = [(0, 0)]

    def update(self, val):
        """
        update position
        """
        num = int(val[1:])
        if val[0] == 'U':
            for i in range(1, num):
                self._coords.append((self.x, self.y + i))
            self.y += num
        elif val[0] == 'D':
            for i in range(1, num):
                self._coords.append((self.x, self.y - i))
            self.y -= num
        elif val[0] == 'R':
            for i in range(1, num):
                self._coords.append((self.x + i, self.y))
            self.x += num
        elif val[0] == 'L':
            for i in range(1, num):
                self._coords.append((self.x - i, self.y))
            self.x -= num

        self._coords.append((self.x, self.y))
        self.length += num

    def pos_length(self, val):
        """
        get position length
        """
        idx = self._coords.index(val)
        return len(self._coords[:idx])

    @property
    def coords(self):
        """
        position history as set
        """
        return set(self._coords)


def manhattan_distance(x, y):
    """
    calculate manhattan distance
    """
    return abs(0-x) + abs(0-y)


def part1(set_1, set_2):
    """
    part 1
    """
    for val in list(set_1.coords & set_2.coords):
        yield manhattan_distance(val[0], val[1])


def part2(line_1, line_2):
    """
    calculate final
    """
    for val in list(line_1.coords & line_2.coords):
        length = line_1.pos_length(val) + line_2.pos_length(val)
        if length > 0:
            yield length


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = [list(d.split(',')) for d in fp.read().splitlines()]

    lines = []
    for idx, d in enumerate(data):
        l = Line(name=idx)
        for val in d:
            l.update(val)
        lines.append(l)

    print(f'shortest manhattan distance: {sorted(part1(lines[0], lines[1]))[1]}')
    print(f'shortest overall intersection: {sorted(part2(lines[0], lines[1]))[0]}')


if __name__ == '__main__':
    main()
