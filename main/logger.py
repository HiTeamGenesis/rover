from colorama import init, Fore, Back, Style
from datetime import datetime
import os 


def debug(msg: str) -> None:
    print(Fore.WHITE + "DEBUG: " + msg)
    pass

def info(msg: str) -> None:
    print(Fore.YELLOW + msg)
    save(msg)
    pass

def success(msg: str) -> None:
    print(Fore.GREEN + msg)
    save(msg)
    pass

def warn(msg: str) -> None:
    print(Fore.RED + "WARNING: " + Fore.YELLOW + msg)
    save(msg)
    pass

def error(msg: str) -> None:
    print(Fore.RED + "ERROR: " + msg)
    save(msg)
    pass

def save(message: str) -> None:
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg_to_log = time + ' | ' + message + "\n"
    logpath = os.path.expanduser('~') + "/LOGS.txt"
    with open(logpath,"a+") as f:
        f.write(msg_to_log)