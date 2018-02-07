#!/usr/bin/env python
# -*- coding: utf-8 -*-
firewall = "0: 4\n1: 2\n2: 3\n4: 5\n6: 8\n8: 4\n10: 6\n12: 6\n14: 6\n16: 10\n18: 6\n20: 12\n22: 8\n24: 9\n26: 8\n28: 8\n30: 8\n32: 12\n34: 12\n36: 12\n38: 8\n40: 10\n42: 14\n44: 12\n46: 14\n48: 12\n50: 12\n52: 12\n54: 14\n56: 14\n58: 14\n60: 12\n62: 14\n64: 14\n68: 12\n70: 14\n74: 14\n76: 14\n78: 14\n80: 17\n82: 28\n84: 18\n86: 14"
#firewall = "0: 3\n1: 2\n4: 4\n6: 4"


# single line cause YOLO
def puzzle1():
    return sum([((int(layer.split(":")[0])) % (2 * (int(layer.split(":")[1]) - 1)) == 0) * int(layer.split(":")[0]) * int(layer.split(":")[1]) for layer in firewall.split("\n")])


def puzzle2():
    i = 0
    while True:
        failed = False
        for layer in firewall.split("\n"):
            if (int(layer.split(":")[0]) + i) % (2 * (int(layer.split(":")[1]) - 1)) == 0: 
                failed = True
                break
        
        if not failed: return i
        i += 1


if __name__ == "__main__":
    print("1: {}".format(puzzle1()))
    print("2: {}".format(puzzle2()))