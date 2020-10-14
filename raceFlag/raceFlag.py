import ac
import acsys
import os
import platform
import sys

"""
"""

"""Load shared libraries"""
if platform.architecture()[0] == "64bit":
  sysdir = "stdlib64"
else:
  sysdir = "stdlib"
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib", sysdir))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
os.environ['PATH'] = os.environ['PATH'] + ";."
from sim_info import info

# Flag values
AC_NO_FLAG = 0
AC_BLUE_FLAG = 1
AC_YELLOW_FLAG = 2
AC_BLACK_FLAG = 3
AC_WHITE_FLAG = 4
AC_CHECKERED_FLAG = 5
AC_PENALTY_FLAG = 6

# Constants
APP_NAME = "Race Flag"
TEXTURE_DIR = "apps/python/raceFlag/textures/"

# Configs
WINDOW_WIDTH = 160
WINDOW_HEIGHT = 120
SHOW_FLAG_NAME = False

# Global variables
flag_label = None
appWindow = None
    

def flag_to_name(flag_value):
    if flag_value == AC_NO_FLAG:
        return "No Flag"
    elif flag_value == AC_BLUE_FLAG:
        return "Blue"
    elif flag_value == AC_YELLOW_FLAG:
        return "Yellow"
    elif flag_value == AC_BLACK_FLAG:
        return "Black"
    elif flag_value == AC_WHITE_FLAG:
        return "White"
    elif flag_value == AC_CHECKERED_FLAG:
        return "Checkered"
    elif flag_value == AC_PENALTY_FLAG:
        return "Penality"
    raise ValueError("Unknown racing flag value '{}'".format(flag_value))
    

def set_bg_texture_by_flag(appWindow, flag_value):
    texture_file = ""
    if flag_value == AC_NO_FLAG:
        texture_file = "empty.png"
    elif flag_value == AC_BLUE_FLAG:
        texture_file = "blue.png"
    elif flag_value == AC_YELLOW_FLAG:
        texture_file = "yellow.png"
    elif flag_value == AC_BLACK_FLAG:
        texture_file = "black.png"
    elif flag_value == AC_WHITE_FLAG:
        texture_file = "white.png"
    elif flag_value == AC_CHECKERED_FLAG:
        texture_file = "chequered.png"
    elif flag_value == AC_PENALTY_FLAG:
        texture_file = "black_white.png"
    else:
        raise ValueError("Unknown racing flag value '{}'".format(flag_value))
    
    texture_path = TEXTURE_DIR + texture_file
    
    ac.setBackgroundTexture(appWindow, texture_path)
    
    
def acMain(ac_version):
    global test_label, appWindow

    appWindow = ac.newApp(APP_NAME)
    ac.setSize(appWindow, WINDOW_WIDTH, WINDOW_HEIGHT)
    ac.drawBorder(appWindow, 0)
    ac.setBackgroundOpacity(appWindow, 0)

    flag_label = ac.addLabel(appWindow, "")
    ac.setPosition(flag_label, 3, 30)
    
    return APP_NAME
    
    
def acUpdate(deltaT):
    global flag_label, appWindow

    flag = info.graphics.flag
    set_bg_texture_by_flag(appWindow, flag)
    if SHOW_FLAG_NAME:
        ac.setText(flag_label, flag_to_name(flag))
