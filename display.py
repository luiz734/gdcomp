from colorama import Fore, Back, Style


def text(msg, prefix=""):
    output = f"{Fore.WHITE}{Back.RESET}{Style.BRIGHT}{prefix} :" if prefix != "" else ""
    output += f"{Fore.WHITE}{Back.RESET}{Style.NORMAL}{msg}"
    print(output)


def warn(msg, prefix=""):
    output = (
        f"{Fore.YELLOW}{Back.RESET}{Style.BRIGHT}{prefix} :" if prefix != "" else ""
    )
    output += f"{Fore.YELLOW}{Back.RESET}{Style.NORMAL}{msg}"
    print(output)


def success(msg, prefix=""):
    output = f"{Fore.GREEN}{Back.RESET}{Style.BRIGHT}{prefix} :" if prefix != "" else ""
    output += f"{Fore.GREEN}{Back.RESET}{Style.NORMAL}{msg}"
    print(output)
