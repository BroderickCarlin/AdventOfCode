#!/usr/bin/env python
# -*- coding: utf-8 -*-
blocks = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]

def puzzle1():
    b = blocks[:]
    past_blocks = []

    count = 0

    while True:
        m = b[0]
        m_idx = 0

        # find current max according to rules
        for i in range(1, len(b)):
            if b[i] > m:
                m = b[i]
                m_idx = i

        b[m_idx] = 0
        m_idx += 1

        if m_idx >= len(b):
            m_idx = 0

        for _ in range(m):
            b[m_idx] += 1
            m_idx += 1
            if m_idx >= len(b):
                m_idx = 0

        count += 1

        for record in past_blocks:
            if record == b:
                return count

        past_blocks.append(b[:])


def puzzle2():
    b = blocks[:]
    past_blocks = []

    count = 0

    while True:
        m = b[0]
        m_idx = 0

        # find current max according to rules
        for i in range(1, len(b)):
            if b[i] > m:
                m = b[i]
                m_idx = i

        b[m_idx] = 0
        m_idx += 1

        if m_idx >= len(b):
            m_idx = 0

        for _ in range(m):
            b[m_idx] += 1
            m_idx += 1
            if m_idx >= len(b):
                m_idx = 0

        count += 1

        for i in range(len(past_blocks)):
            if past_blocks[i] == b:
                return len(past_blocks) - i

        past_blocks.append(b[:])


if __name__ == "__main__":
    print("1: {}".format(puzzle1()))
    print("2: {}".format(puzzle2()))