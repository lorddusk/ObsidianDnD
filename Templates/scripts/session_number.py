import sys
import traceback


def main():
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("Error when running user template.")
        print("```")
        traceback.print_exc(file=sys.stdout)
        print("```")