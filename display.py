from colorama import Fore, Back, Style


def text(msg, prefix=""):
    output = f"{Fore.WHITE}{Back.RESET}{Style.BRIGHT}{prefix} :" if prefix != "" else ""
    output += f"{Fore.WHITE}{Back.RESET}{Style.NORMAL}{msg}"
    print(output)


def bright(msg, prefix=""):
    print(Style.RESET_ALL, end="")
    output = f"{Fore.WHITE}{Back.RESET}{Style.BRIGHT}{prefix} :" if prefix != "" else ""
    output += f"{Fore.WHITE}{Back.RESET}{Style.BRIGHT}{msg}"
    print(output)


def dimmed(msg, prefix=""):
    print(Style.RESET_ALL, end="")
    output = f"{Fore.WHITE}{Back.RESET}{Style.DIM}{prefix} :" if prefix != "" else ""
    output += f"{Fore.WHITE}{Back.RESET}{Style.DIM}{msg}"
    print(output)


def warn(msg, prefix=""):
    print(Style.RESET_ALL, end="")
    output = (
        f"{Fore.YELLOW}{Back.RESET}{Style.BRIGHT}{prefix} :" if prefix != "" else ""
    )
    output += f"{Fore.YELLOW}{Back.RESET}{Style.NORMAL}{msg}"
    print(output)


def success(msg, prefix=""):
    print(Style.RESET_ALL, end="")
    output = f"{Fore.GREEN}{Back.RESET}{Style.BRIGHT}{prefix} :" if prefix != "" else ""
    output += f"{Fore.GREEN}{Back.RESET}{Style.NORMAL}{msg}"
    print(output)
