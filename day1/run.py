#!/usr/bin/env/python3


def calc_fuel(val):
    return int(val/3)-2

def fuel_mass(val):
    output = 0
    while True:
        val = calc_fuel(val)
        output += val
        if not val > 6:
            return output


def main():
    with open('input.txt') as fp:
        data = fp.readlines()

    print(sum([calc_fuel(int(l.strip())) for l in data]))
    print(sum([fuel_mass(int(l.strip())) for l in data]))


if __name__ == '__main__':
    main()
