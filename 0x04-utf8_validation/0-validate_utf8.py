#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers represents valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    remaining_bytes = 0
    data_length = len(data)

    # Iterate through the list of integers
    for index in range(data_length):
        # Skip processing if there are remaining bytes from a multi-byte char
        if remaining_bytes > 0:
            remaining_bytes -= 1
            continue

        # Validate the current integer
        current_integer = data[index]
        if (type(current_integer) != int or current_integer < 0
           or current_integer > 0x10ffff):
            return False
        elif current_integer <= 0x7f:
            remaining_bytes = 0
        elif current_integer & 0b11111000 == 0b11110000:
            # 4-byte UTF-8 character encoding
            expected_bytes = 4
            if data_length - index >= expected_bytes:
                # Check the format of subsequent bytes
                valid_body = all(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[index + 1: index + expected_bytes],
                ))
                if not valid_body:
                    return False
                remaining_bytes = expected_bytes - 1
            else:
                return False
        elif current_integer & 0b11110000 == 0b11100000:
            # 3-byte UTF-8 character encoding
            expected_bytes = 3
            if data_length - index >= expected_bytes:
                # Check the format of subsequent bytes
                valid_body = all(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[index + 1: index + expected_bytes],
                ))
                if not valid_body:
                    return False
                remaining_bytes = expected_bytes - 1
            else:
                return False
        elif current_integer & 0b11100000 == 0b11000000:
            # 2-byte UTF-8 character encoding
            expected_bytes = 2
            if data_length - index >= expected_bytes:
                # Check the format of subsequent bytes
                valid_body = all(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[index + 1: index + expected_bytes],
                ))
                if not valid_body:
                    return False
                remaining_bytes = expected_bytes - 1
            else:
                return False
        else:
            return False

    # All characters are valid UTF-8 codepoints
    return True
