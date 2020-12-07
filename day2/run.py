#!/usr/bin/env python3
import itertools


def calc_intcode(codes, noun=None, verb=None):
    """
    calculate intcode
    """
    codes = codes.copy()
    if noun:
        codes[1] = noun

    if verb:
        codes[2] = verb

    for idx in range(0, len(codes), 4):
        try:
            if codes[idx] == 99:
                break
            v1 = codes[codes[idx+1]]
            v2 = codes[codes[idx+2]]
            position = codes[idx+3]
            if codes[idx] == 1:
                codes[position] = v1 + v2
            elif codes[idx] == 2:
                codes[position] = v1 * v2
        except IndexError:
            break

    return codes[0]


def main():
    """
    main
    """
    with open('input.txt') as fp:
        codes = [int(f) for f in fp.read().split(',')]

    print(f'part 1: {calc_intcode(codes, 12, 2)}')

    for noun, verb in itertools.product(range(100), range(100)):
        if calc_intcode(codes, noun, verb) == 19690720:
            print(f'part 2: noun={noun} verb={verb} result={100*noun+verb}')
            break


if __name__ == '__main__':
    main()
