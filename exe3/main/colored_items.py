import sys
from pathlib import Path

# ANSI color codes for text colors
COLOR_RED = '\033[91m'   # Red color
COLOR_CYAN = '\033[96m'  # Cyan color
COLOR_RESET = '\033[0m'  # Reset color to default

def print_directory_contents(directory, indent='    ', color=''):
    path = Path(directory)

    if not path.is_dir():
        print(f"The path '{directory}' is not a valid directory.")
        return
    
    print(f"Contents of directory '{directory}':")
    print_files_recursive(path, indent, color)

def print_files_recursive(directory, indent='', color=''):
    for entry in sorted(directory.iterdir()):
        if entry.is_dir():
            if not entry.name.startswith("."):  # ігнорувати системні файли
                print(f"{indent}{COLOR_CYAN}{entry.name}/{COLOR_RESET}")
                print_files_recursive(entry, indent + '    ', color)
        elif entry.is_file():
            if not entry.name.startswith("."):  # ігнорувати системні файли
                print(f"{indent}{color}{entry.name}{COLOR_RESET}")

if __name__ == "__main__":
    # Перевіряємо, чи є переданий шлях до директорії через аргумент командного рядка
    if len(sys.argv) < 2:
        print("Usage: python print_directory_contents.py <directory>")
        sys.exit(1)
    
    # Отримуємо шлях до директорії з аргумента командного рядка
    directory_path = sys.argv[1]
    
    # Викликаємо функцію для друку вмісту директорії з використанням червоного кольору
    print_directory_contents(directory_path, color=COLOR_RED)
