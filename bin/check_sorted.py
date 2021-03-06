#!/usr/bin/env python
import fileinput
import re

"""
Check if each section separated by comment has alphabetically sorted lines.
"""
prev_line = None
for line in fileinput.input():
    line = line.strip()
    if not line or line.startswith('!') or re.match(r'\[Adblock.*\]', line):
        prev_line = None
        continue
    if not prev_line:
        prev_line = line
        continue
    if prev_line >= line:
        raise Exception('This line is not sorted: ' + line)
    prev_line = line
