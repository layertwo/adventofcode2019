#!/usr/bin/env python3
import itertools
from pprint import pprint

def calc_intcode(codes):
    for r in range(0, len(codes), 4):
        val = codes[r]
        position = codes[r+3]
        try:
            if val == 1:
                res = codes[codes[r+1]] + codes[codes[r+2]]
                codes[position] = res
            elif val == 2:
                res = codes[codes[r+1]] * codes[codes[r+2]]
                codes[position] = res
            elif val == 99:
                break
        except IndexError:
            break

    return codes


def gravity_assist(codes, noun, verb):
    codes[1] = noun
    codes[2] = verb
    return calc_intcode(codes)


def main():
    with open('input.txt') as fp:
        opcodes = [int(f) for f in fp.read().split(',')]

    part1 = opcodes.copy()
    # fixup list
    part1[1] = 12
    part1[2] = 2
    result = calc_intcode(part1)
    print(result)
    print(result[0])

    for noun, verb in itertools.product(range(0,100), range(0,100)):
        codes = opcodes.copy()
        val = gravity_assist(codes, noun, verb)
        if val[0] == 19690720:
            print('found it!')
            print('noun = {}, verb = {}'.format(noun, verb))
            print(100*noun + verb)


if __name__ == '__main__':
    main()
