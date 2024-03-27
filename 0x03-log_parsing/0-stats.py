#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys
import signal
import re

# Initialize metrics
total_size = 0
# Pre-defined status codes are initialized to zero
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Define the pattern for the log line
pattern = (
        r'(\d+\.\d+\.\d+\.\d+) - \[(.+)\] "GET /projects/260 HTTP/1.1" '
        r'(\d+) (\d+)'
)


def print_metrics(signum=None, frame=None):
    """Function to print metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# Set the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, print_metrics)

# Read stdin line by line
for i, line in enumerate(sys.stdin, start=1):
    match = re.match(pattern, line)
    if match:
        # Update metrics
        total_size += int(match.group(4))  # File size
        status_code = int(match.group(3))  # Status code
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            # Handle unexpected status codes by not doing anything
            pass

    # Print metrics every 10 lines
    if i != 0 and i % 10 == 0:
        print_metrics()

# Print final metrics
print_metrics()
