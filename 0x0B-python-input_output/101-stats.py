#!/usr/bin/python3

""" module Write a script that reads stdin line by line and computes metrics.
"""
import sys


def print_data(status_codes: dict, file_size: int):
    """ print data to stdout
        Args:
            status_codes: a dict with status codes
            file_size: the size of file
    """
    sys.stdout.write(f"File size: {file_size}\n")
    for x, y in status_codes.items():
        sys.stdout.write(f"{x}: {y}\n")
        sys.stdout.flush()
    sys.stdout.flush()


def get_metrics():
    """ script that reads stdin line by line and computes metrics
    """
    file_size = 0
    line_count = 0

    status_codes = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
            }

    try:
        for line in sys.stdin:
            for j in status_codes:
                if j in line:
                    status_codes[j] += 1
            status = line.strip("\n").split(" ")
            if line_count > 0 and line_count % 10 == 0:
                print_data(status_codes, file_size)

            file_size += int(status[-1])
            line_count += 1

    except KeyboardInterrupt:
        print_data(status_codes, file_size)
        raise


get_metrics()
