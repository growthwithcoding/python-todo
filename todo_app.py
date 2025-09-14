
from typing import List, Dict, Tuple, Optional
from colorama import init as colorama_init, Fore, Style
from pathlib import Path

# Initialize color support for Windows terminals (PowerShell, cmd) and others
colorama_init(autoreset=True)

DATA_FILE = Path("tasks.txt")
IMPORTANCE_ORDER = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}

# ---- Persistence ----
def load_tasks() -> List[Dict[str, str]]:
    """Load tasks from the text file into a list. Each line is 'importance|task'."""
    tasks: List[Dict[str, str]] = []
    if not DATA_FILE.exists():
        return tasks
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                # Expect "importance|task text"
                parts = line.split("|", 1)
                if len(parts) != 2:
                    continue
                importance, text = parts
                importance = importance.strip().upper()
                text = text.strip()
                if importance not in {"HIGH", "MEDIUM", "LOW"} or not text:
                    continue
                tasks.append({"text": text, "importance": importance})
    except Exception as e:
        print(f"{Fore.RED}✖ Failed to load tasks: {e}")
    return tasks

def save_tasks(tasks: List[Dict[str, str]]) -> None:
    """Persist tasks to the text file, one per line as 'importance|task'."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            for t in tasks:
                f.write(f"{t['importance']}|{t['text']}\n")
    except Exception as e:
        print(f"{Fore.RED}✖ Failed to save tasks: {e}")

# ---- UI Helpers ----
def color_for_importance(importance: str) -> Tuple[str, str]:
    """Return (color_code, label) for the given importance level."""
    imp = importance.upper()
    if imp == "HIGH":
        return Fore.RED, "HIGH"
    if imp == "MEDIUM":
        return Fore.YELLOW, "MEDIUM"
    return Fore.GREEN, "LOW"

def sorted_indices_by_importance(tasks: List[Dict[str, str]]) -> List[int]:
    """Return a list of indices representing tasks sorted High → Medium → Low (stable)."""
    return sorted(
        range(len(tasks)),
        key=lambda i: (IMPORTANCE_ORDER.get(tasks[i]["importance"], 3), i)
    )

def print_welcome() -> None:
    """Print the welcome banner."""
    print(f"{Style.BRIGHT}{Fore.CYAN}Welcome to the To-Do CLI!")
    print(f"{Fore.BLUE}Manage your tasks right from the terminal.\n")

def print_menu() -> None:
    """Display the main menu options."""
    print(f"\n{Style.BRIGHT}{Fore.MAGENTA}Main Menu")
    print(f"{Fore.WHITE}[1]{Fore.GREEN} Add a task")
    print(f"{Fore.WHITE}[2]{Fore.YELLOW} View tasks (High → Medium → Low)")
    print(f"{Fore.WHITE}[3]{Fore.RED} Delete a task")
    print(f"{Fore.WHITE}[4]{Fore.CYAN} Quit")

def get_choice() -> str:
    """Prompt the user for a menu selection."""
    return input(f"\n{Fore.WHITE}Enter a choice (1-4): ").strip()

# ---- Core Features ----
def prompt_importance() -> Optional[str]:
    """Prompt for importance with retry and cancel support.
    Returns HIGH/MEDIUM/LOW, or None if the user cancels."""
    while True:
        print(f"{Fore.WHITE}Select importance: {Fore.GREEN}[L]ow{Fore.WHITE} / {Fore.YELLOW}[M]edium{Fore.WHITE} / {Fore.RED}[H]igh {Fore.WHITE}/ [C]ancel")
        raw = input(f"{Fore.WHITE}Enter H, M, L, or C to cancel: ").strip().lower()
        if raw in {"c", "cancel"}:
            print(f"{Fore.BLUE}Canceled. Returning to the main menu.")
            return None
        if raw in {"h", "high"}:
            return "HIGH"
        if raw in {"m", "med", "medium"}:
            return "MEDIUM"
        if raw in {"l", "low"}:
            return "LOW"
        print(f"{Fore.RED}✖ Invalid choice. Please enter H, M, L, or C.")

def add_task(tasks: List[Dict[str, str]]) -> None:
    """Add a new task with importance to the list and save to file (supports cancel and retries)."""
    # Task text loop with cancel
    while True:
        text = input(f"{Fore.GREEN}Enter a new task (or C to cancel): ").strip()
        if text.lower() in {"c", "cancel"}:
            print(f"{Fore.BLUE}Canceled. Returning to the main menu.")
            return
        if text:
            break
        print(f"{Fore.RED}✖ Task cannot be empty. Try again or C to cancel.")
    # Importance loop
    importance = prompt_importance()
    if importance is None:
        return
    tasks.append({"text": text, "importance": importance})
    save_tasks(tasks)
    color, label = color_for_importance(importance)
    print(f"{color}✔ Added ({label}): {Fore.WHITE}{text}")

def view_tasks(tasks: List[Dict[str, str]]) -> None:
    """View all tasks sorted by importance, or show a friendly message if none exist."""
    if not tasks:
        print(f"{Fore.BLUE}Your list is empty — add your first task from the menu!")
        return
    print(f"\n{Style.BRIGHT}{Fore.YELLOW}Your Tasks (High → Medium → Low):")
    for disp_idx, i in enumerate(sorted_indices_by_importance(tasks), start=1):
        t = tasks[i]
        color, label = color_for_importance(t["importance"])
        print(f"  {Fore.WHITE}{disp_idx}. {color}[{label}]{Fore.WHITE} {t['text']}")

def delete_task(tasks: List[Dict[str, str]]) -> None:
    """Delete a task by its displayed number (sorted view) with retries and cancel option."""
    if not tasks:
        print(f"{Fore.RED}✖ No tasks to delete.")
        return

    # Build the sorted display and show it
    sorted_idxs = sorted_indices_by_importance(tasks)
    print(f"\n{Style.BRIGHT}{Fore.YELLOW}Your Tasks (High → Medium → Low):")
    for disp_idx, i in enumerate(sorted_idxs, start=1):
        t = tasks[i]
        color, label = color_for_importance(t["importance"])
        print(f"  {Fore.WHITE}{disp_idx}. {color}[{label}]{Fore.WHITE} {t['text']}")

    # Input loop: retry on invalid, allow cancel
    while True:
        raw = input(f"\n{Fore.RED}Enter the displayed task number to delete ({Fore.WHITE}or C to cancel{Fore.RED}): ").strip()
        if raw.lower() in {"c", "cancel"}:
            print(f"{Fore.BLUE}Canceled. Returning to the main menu.")
            return
        try:
            disp_index = int(raw)
            if disp_index < 1 or disp_index > len(sorted_idxs):
                print(f"{Fore.RED}✖ That task number doesn't exist. Try again or C to cancel.")
                continue
        except ValueError:
            print(f"{Fore.RED}✖ Please enter a valid number, or C to cancel.")
            continue
        # Valid selection
        real_index = sorted_idxs[disp_index - 1]
        removed = tasks.pop(real_index)
        save_tasks(tasks)
        color, label = color_for_importance(removed["importance"])
        print(f"{color}🗑 Deleted ({label}): {Fore.WHITE}{removed['text']}")
        break

    # Always show remaining tasks (sorted)
    if tasks:
        print(f"\n{Fore.CYAN}Remaining tasks (High → Medium → Low):")
        for disp_idx, i in enumerate(sorted_indices_by_importance(tasks), start=1):
            t = tasks[i]
            c, l = color_for_importance(t["importance"])
            print(f"  {Fore.WHITE}{disp_idx}. {c}[{l}]{Fore.CYAN} {t['text']}")
    else:
        print(f"{Fore.BLUE}Your list is now empty.")

def main() -> None:
    """Run the interactive To-Do CLI application with persistence."""
    tasks: List[Dict[str, str]] = load_tasks()
    print_welcome()
    # Show tasks immediately on startup (or a friendly message if none)
    view_tasks(tasks)

    while True:
        print_menu()
        choice = get_choice()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print(f"\n{Fore.CYAN}Goodbye! 👋")
            break
        else:
            print(f"{Fore.RED}✖ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
