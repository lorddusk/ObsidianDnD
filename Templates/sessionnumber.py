#!/usr/bin/python3

import sys
import traceback
from pathlib import Path


def increase_session_number():
    path = Path(r"sessionnumber.txt")
    with open(path, 'r') as f:
        number = int(f.read())
    number += 1
    with open(path, 'w') as f2:
        f2.write(f'{str(number)}')
    print(number)


def main():
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    increase_session_number()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("Error when running user template.")
        print("```")
        traceback.print_exc(file=sys.stdout)
        print("```")
