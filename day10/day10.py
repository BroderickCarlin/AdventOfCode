#!/usr/bin/env python
# -*- coding: utf-8 -*-
lengths = "187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216"
suffix = [17, 31, 73, 47, 23]
num_rounds = 64

def puzzle1():
    knot = range(256)
    skip_size = 0
    idx1 = 0

    for l in [int(a) for a in lengths.split(",")]:
        idx2 = idx1 + l

        k = []
        if idx2 >= len(knot): 
            k = knot[idx1:] + knot[:idx2 - len(knot)]
        else:
            k = knot[idx1:idx2]

        k = list(reversed(k))
        if idx2 >= len(knot): 
            knot[idx1:] = k[:len(knot) - idx1]
            knot[:idx2 - len(knot)] = k[len(knot) - idx1:]
        else:
            knot[idx1:idx2] = k

        idx1 += skip_size + l
        while idx1 >= len(knot): idx1 -= len(knot)
        skip_size += 1

    return knot[0] * knot[1]


def puzzle2():
    knot = range(256)
    hash_knot = ""
    skip_size = 0
    idx1 = 0

    for _ in range(num_rounds):
        for l in list(bytearray(lengths)) + suffix:
            idx2 = idx1 + l

            k = []
            if idx2 >= len(knot): 
                k = knot[idx1:] + knot[:idx2 - len(knot)]
            else:
                k = knot[idx1:idx2]

            k = list(reversed(k))
            if idx2 >= len(knot): 
                knot[idx1:] = k[:len(knot) - idx1]
                knot[:idx2 - len(knot)] = k[len(knot) - idx1:]
            else:
                knot[idx1:idx2] = k

            idx1 += skip_size + l
            while idx1 >= len(knot): idx1 -= len(knot)
            skip_size += 1

    for x in range(16):
        s = 0
        for y in range(16):
            s ^= knot[x * 16 + y]
        hash_knot += "%0.2X" % s

    return hash_knot

if __name__ == "__main__":
    print("1: {}".format(puzzle1()))
    print("2: {}".format(puzzle2()))
