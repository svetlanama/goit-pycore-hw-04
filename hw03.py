import sys
from pathlib import Path
from colorama import init, Fore, Style


# Task 3:
def print_directory_tree(path: Path, indent: str = ""):
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
            print_directory_tree(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main():
    init(autoreset=True)
    if len(sys.argv) < 2:
        print("Specify the path to the directory as a command-line argument.")
        sys.exit(1)
    dir_path = Path(sys.argv[1])
    if not dir_path.exists():
        print(f"Path not fround: {dir_path}")
        sys.exit(1)
    if not dir_path.is_dir():
        print(f"Path is not a directory: {dir_path}")
        sys.exit(1)
    print(f"Directory structure: {dir_path}:")
    print_directory_tree(dir_path)


if __name__ == "__main__":
    main()
