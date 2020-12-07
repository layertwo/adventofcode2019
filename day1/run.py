#!/usr/bin/env python3


def calc_fuel(data):
    """
    calc fuel
    """
    for val in data:
        yield int(val/3)-2


def fuel_mass(data):
    """
    fuel mass
    """
    for val in data:
        output = 0
        while True:
            val = int(val/3)-2
            output += val
            if not val > 6:
                yield output
                output = 0
                break


def main():
    with open('input.txt') as fp:
        data = [int(line) for line in fp.read().splitlines()]

    print(sum(calc_fuel(data)))
    print(sum(fuel_mass(data)))


if __name__ == '__main__':
    main()
