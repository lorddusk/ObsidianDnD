import sys
import traceback
from pathlib import Path

template_folder = 'Templates'


def main():
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    path = Path(r"session_number.txt")
    file = open(path, "w+")
    number = file.read()
    newNumber = f"{int(number) + 1}"
    file.write(newNumber)
    file.close()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("Error when running user template.")
        print("```")
        traceback.print_exc(file=sys.stdout)
        print("```")
