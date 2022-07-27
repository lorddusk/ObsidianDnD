import sys
import traceback

template_folder = 'Templates'

def main():
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    file = open("session_number.txt", "W+")
    number = file.read()
    newNumber = f"{number + 1}"
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