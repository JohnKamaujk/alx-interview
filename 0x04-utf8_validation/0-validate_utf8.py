#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            skip = 0
        else:
            num_leading_ones = bin(data[i] & 0xff).index('0') - 2
            if num_leading_ones == 1:
                return False
            byte_count = max(1, num_leading_ones)
            if n - i >= byte_count:
                next_body = all(0b10000000 <= x <= 0b10111111 for x in
                                data[i + 1: i + byte_count])
                if not next_body:
                    return False
                skip = byte_count - 1
            else:
                return False
    return True
