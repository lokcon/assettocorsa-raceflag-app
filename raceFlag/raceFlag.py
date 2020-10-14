import ac
import acsys
from utils import load_shared_libraries
load_shared_libraries()
from sim_info import info


# Flag values (from ctypes used by Assetto Corsa shared memory)
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
BACKGROUND_OPACITY = 0.1

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
    ac.setBackgroundOpacity(appWindow, BACKGROUND_OPACITY)


def set_flag_label_by_flag(flag_label, flag_value):
    if SHOW_FLAG_NAME:
        ac.setText(flag_label, flag_to_name(flag_value))
    
    
def acMain(ac_version):
    global flag_label, appWindow

    # Initialise app
    appWindow = ac.newApp(APP_NAME)
    ac.setSize(appWindow, WINDOW_WIDTH, WINDOW_HEIGHT)
    ac.drawBorder(appWindow, 0)
    ac.setBackgroundOpacity(appWindow, BACKGROUND_OPACITY)

    # Add flag label text widget
    flag_label = ac.addLabel(appWindow, "")
    ac.setPosition(flag_label, 3, 30)

    # Test texture
    # texture = ac.newTexture(TEXTURE_DIR + "blue.png")
    # ac.setPosition(texture, 0, 30)
    
    return APP_NAME
    
    
def acUpdate(deltaT):
    global flag_label, appWindow

    flag = info.graphics.flag

    set_bg_texture_by_flag(appWindow, flag)
    set_flag_label_by_flag(flag_label, flag)
