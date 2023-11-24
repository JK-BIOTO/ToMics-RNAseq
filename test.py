#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_

import sys

class nums:
    def xx(i):
        """makes double

        Args:
            i (int): integer
        """
        return i + i + i


def test():
    for i in range(10):
        print(nums.xx(i))
    return None


if __name__ == "__main__":
    test()