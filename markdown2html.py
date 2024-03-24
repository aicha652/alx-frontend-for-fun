#!/usr/bin/python3
"""script that takes 2 arguments First one is
the name of the Markdown file, the second is the
output file name"""
import sys
import os.path


if __name__ == "__main__":
    """create a script"""
    if (len(sys.argv) < 2):
        print('Usage: ./markdown2html.py'
              ' README.md README.html', file=sys.stderr)
        exit(1)
    elif (os.path.isfile(sys.argv[1]) is False):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)
    else:
        exit(0)
