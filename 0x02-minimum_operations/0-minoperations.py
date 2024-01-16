#!/usr/bin/python3
'''Minimum operations coding challenge.
'''


def minOperations(n):
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters using Copy All and Paste operations.
    '''
    if not isinstance(n, int) or n <= 0:
        # Invalid input, return 0 as it's impossible to achieve.
        return 0

    operations_count = 0  # To keep track of the total number of operations.
    clipboard = 0  # The content in the clipboard that can be pasted.
    characters_generated = 1  # The number of 'H' characters generated.

    # Perform operations until the desired number of characters is achieved.
    while characters_generated < n:
        if clipboard == 0:
            # If clipboard is empty, perform an initial Copy All and Paste.
            clipboard = characters_generated
            characters_generated += clipboard
            operations_count += 2
        elif (n - characters_generated) % characters_generated == 0:
            # If the remaining characters can be evenly divided by the
            # current count,
            # perform a Copy All and Paste.
            clipboard = characters_generated
            characters_generated += clipboard
            operations_count += 2
        elif clipboard > 0:
            #Perform a Paste operation.
            characters_generated += clipboard
            operations_count += 1

    return operations_count
