import platform
import os
import sys


def load_shared_libraries():
    if platform.architecture()[0] == "64bit":
      sysdir = "stdlib64"
    else:
      sysdir = "stdlib"

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib", sysdir))
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
    os.environ['PATH'] = os.environ['PATH'] + ";."
