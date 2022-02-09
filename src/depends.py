import subprocess
import platform
import socket
import time
import os
from clint.textui import puts,colored
from creativness import cursives
if platform.system == "linux":
    import readline 
    import rlcompleter 
    import atexit
import distro
import random
from src import define
from src import etc
from datetime import datetime
import sys
sys.path.insert(0, '../')