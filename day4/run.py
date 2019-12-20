#!/usr/bin/env python3
MIN = 231832
MAX = 767346

def calc_unique(num):
    num = [int(n) for n in str(num)]
    count = 0
    for idx, n in enumerate(num):
        try:
            if num[idx+1] < n:
                return False
            if n == num[idx+1]:
                count += 1
        except IndexError:
            if n < num[idx-1]:
                return False

    if count == 0:
        return False
    return True


def calc_unique2(num):
    num = [int(n) for n in str(num)]
    count = 0
    occurences = {}
    for idx, n in enumerate(num):
        if n in occurences:
            occurences[n] += 1
        else:
            occurences[n] = 1

        try:
            if num[idx+1] < n:
                return False
        except IndexError:
            if n < num[idx-1]:
                return False
        try:
            if n == num[idx+1]:
                count += 1
        except IndexError:
            pass

    if count == 0:
        return False

    if 2 in list(occurences.values()):
        return True
    return False


def main():
    part1 = [num for num in range(MIN, MAX+1) if calc_unique(num)]
    print(len(part1))
    part2 = [num for num in range(MIN, MAX+1) if calc_unique2(num)]
    print(len(part2))


if __name__ == '__main__':
    main()
