from src import depends

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        depends.time.sleep(1)
        t -= 1

def distro(cd):
    if depends.distro.id() == "ubuntu" or depends.distro.id() == "debian":
        depends.os.system("sudo apt install"+cd)
    elif depends.distro.id() == "arch":
        depends.os.system("pacman -S"+cd)
    elif depends.distro.id() == "centos" or depends.distro.id() == "rehl":
        depends.os.system("yum install"+cd)
    elif depends.distro.id() == "fedora":
        depends.os.system("dnf install"+cd)
    elif depends.distro.id() == "opensuse":
        depends.os.system("zypper install"+cd)
    elif depends.distro.id() == "gentoo":
        depends.os.system("emerge --ask"+cd)
    elif depends.distro.id() == "void":
        depends.os.system("xbps-install -S"+cd)
    elif depends.distro.id() == "solus":
        depends.os.system("eopkg install"+cd)
    elif depends.platform.system() == "Windows":
        depends.os.system("winget install"+cd)