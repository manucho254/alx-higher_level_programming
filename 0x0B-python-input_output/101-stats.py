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

    status_codes = {}

    try:
        for line in sys.stdin:
            message = line.split()
            line_count += 1

            # if len(message) less than 2 go to the next iteration
            if len(message) < 2:
                line_count += 1
                continue

            code = message[-2]  # status code
            size = message[-1]  # file size

            if code.isnumeric():
                if code not in status_codes:
                    status_codes[code] = 1
                else:
                    status_codes[code] += 1

            if size.isnumeric():
                file_size += int(size)

            if line_count % 10 == 0:
                print_data(dict(sorted(status_codes.items())), file_size)

        # for cases where we have only one line in file
        if line_count == 1 or len(status_codes) == 0:
            print_data(status_codes, file_size)

    except KeyboardInterrupt:
        print_data(dict(sorted(status_codes.items())), file_size)
        raise


get_metrics()
