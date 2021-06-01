#!/usr/bin/python3
""" this module reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
    - Total file size: File size: <total size>
    - Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        in format: <status code>: <number>
"""
import fileinput


def print_stats(total_bytes, status):
    """prints the stats in format:
        File size: <total size>
        <status code>: <number>
    """
    stats = "File size: {}\n".format(total_bytes)
    for status_code in status.keys():
        stats += "{}: {}\n".format(status_code, status[status_code])
    print(stats, end='')


total_bytes = 0
# status is a dict status_code: counter
status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0


try:
    for raw_line in fileinput.input():
        # uses try to handle the ctrl + c signal
        split_line = raw_line.split()

        total_bytes += int(split_line[-1])

        status_code = split_line[-2]
        if status_code in status.keys():
            status[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_bytes, status)

except KeyboardInterrupt as err:
    # catch the erro, prints the stats and then raises the error
    print_stats(total_bytes, status)
    raise err
