#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    Args:
        input_line (str): A line from the HTTP request log.

    Returns:
        dict: A dictionary containing status code and file size.
    '''
    pattern = (
        r'\s*(?P<ip>\S+)\s*'
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]'
        r'\s*"(?P<request>[^"]*)"\s*'
        r'\s*(?P<status_code>\S+)'
        r'\s*(?P<file_size>\d+)'
    )
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(pattern[0], pattern[1], pattern[2],
                                        pattern[3], pattern[4])
    match = re.fullmatch(log_fmt, input_line)
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    if match:
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    return info

