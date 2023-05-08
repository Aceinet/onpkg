import rich, os, sys
import requests
from rich.console import Console
clear = lambda: os.system('clear')

rawserver = "https://raw.githubusercontent.com/Aceinet/onpkg/main/serverurl.txt"
page = requests.get(rawserver)

usrdir = "~/.." # For termux
#usrdir = "~/../.." # For other unix systems

server = str(page.text).replace("\n", "")
c = Console()
try:
    if sys.argv[1] == "install":
        if sys.argv[2]:
            pkgurl = server + f"/pkgs/{sys.argv[2]}"
            c.print(f"Do you want to [green]install[/green] {sys.argv[2]} package? (y/n)")
            ans = input("> ")
            if ans == "y": 
                os.system(f"wget {pkgurl} -P {usrdir}/bin/")
                os.system(f"chmod +x {usrdir}/bin/{sys.argv[2]}")
    if sys.argv[1] == "nosuremove":
        if sys.argv[2]:
            c.print(f"Do you want to [red]remove[/red] {sys.argv[2]} package? (y/n)")
            ans = input("> ")
            if ans == "y": os.system(f"rm {usrdir}/bin/{sys.argv[2]}")

    if sys.argv[1] == "suremove":
        if sys.argv[2]:
            c.print(f"Do you want to [red]remove[/red] {sys.argv[2]} package? (y/n)")
            ans = input("> ")
            if ans == "y": os.system(f"sudo rm {usrdir}/bin/{sys.argv[2]}")

except IndexError: print("""usage: [option]

options:
    install [package ]    | Install a package
    nosuremove [package]  | Remove a package without sudo rights
    suremove [package]    | Remove a package with sudo rights""")
