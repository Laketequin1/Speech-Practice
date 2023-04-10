import os
import difflib
import time
import math
from colorama import Fore, Style, init

init()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def read_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return text.split('. ')

def print_progress(i, num_lines):
    progress = f" Progress: {i+1}/{num_lines}\n"
    screen_width = os.get_terminal_size().columns
    padding = screen_width - len(progress)
    print('-' * padding, end='')
    print(Fore.GREEN + progress + Style.RESET_ALL, end='\n')

def main():
    file_path = "speech.txt"
    lines = read_file(file_path)
    num_lines = len(lines)
    for i, line in enumerate(lines):
        clear_screen()
        line += '.'  # Add full stop to line
        while True:
            print_progress(i, num_lines)
            print(Fore.CYAN + line + Style.RESET_ALL)
            user_input = input("\nType the line: ")
            accuracy = difflib.SequenceMatcher(None, line.lower(), user_input.lower()).ratio()
            if accuracy < 0.95 and user_input != "pass":
                print(Fore.RED + f"\nPlease try again. Accuracy: {math.floor(accuracy * 1000) / 1000}" + Style.RESET_ALL)
                time.sleep(1)
                input("\n>>> Press Enter to continue...")
                clear_screen()
                continue
            print(Fore.GREEN + f"\nCorrect! Now try without the text." + Style.RESET_ALL)
            time.sleep(0.5)
            clear_screen()
            print_progress(i, num_lines)
            print(Fore.CYAN + line + Style.RESET_ALL)
            time.sleep(0.5)
            input("\n>>> Press Enter to continue...")
            clear_screen()
            print_progress(i, num_lines)
            user_input = input("Type the line: ")
            accuracy = difflib.SequenceMatcher(None, line.lower(), user_input.lower()).ratio()
            if accuracy >= 0.95:
                print(Fore.GREEN + f"\nCorrect! Now try the next sentance." + Style.RESET_ALL)
                time.sleep(0.5)
                break
            else:
                print(Fore.RED + f"\nCorrect answer: {line}" + Style.RESET_ALL)
                print(f"\nPlease try again. Accuracy: {math.floor(accuracy * 1000) / 1000}")
                time.sleep(1)
                input("\n>>> Press Enter to continue...")
                clear_screen()
    print(Fore.GREEN + "Done." + Style.RESET_ALL)

if __name__ == '__main__':
    main()
