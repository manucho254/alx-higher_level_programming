#!/usr/bin/python3

""" module Write a script that reads stdin line by line and computes metrics.
"""
import sys


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
                sys.stdout.write(f"File size: {file_size}\n")
                for x, y in status_codes.items():
                    sys.stdout.write(f"{x}: {y}\n")

            file_size += int(status[-1])
            line_count += 1

    except KeyboardInterrupt:
        sys.stdout.write(f"File size: {file_size}\n")
        for x, y in status_codes.items():
            sys.stdout.write(f"{x}: {y}\n")
        raise


if __name__ == "__main__":
    get_metrics()
