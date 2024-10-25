import sys

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except:
        return 0

if __name__ == "__main__":
    if '--file' in sys.argv:
        file_path = sys.argv[sys.argv.index('--file') + 1]
        print(count_lines(file_path))