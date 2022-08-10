#!/usr/bin/python3
import re
def main():
    pattern = '[0-9]+'
    with open('num.txt') as f:
        for line in f:
            re.findall(pattern, line)

if__name__ == "__main__":
    main()
