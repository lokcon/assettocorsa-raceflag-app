import ac
import acsys
import collections
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
HEADER_HEIGHT = 30
PADDING = 5 
# Configs
WINDOW_WIDTH = 160
WINDOW_HEIGHT = 120
SHOW_FLAG_NAME = False
BACKGROUND_OPACITY = 0.5

# Global variables
flag_label = None
appWindow = None
previous_flag_value = None

# Generate flags
Flag = collections.namedtuple("Flag", ["name", "texture"])
FLAGS = {
    AC_NO_FLAG:        Flag(name="No flag",   texture="blue.png"),
    AC_BLUE_FLAG:      Flag(name="Blue",      texture="blue.png"),
    AC_YELLOW_FLAG:    Flag(name="Yellow",    texture="yellow.png"),
    AC_BLACK_FLAG:     Flag(name="Black",     texture="black.png"),
    AC_WHITE_FLAG:     Flag(name="White",     texture="white.png"),
    AC_CHECKERED_FLAG: Flag(name="Checkered", texture="chequered.png"),
    AC_PENALTY_FLAG:   Flag(name="Penalty",   texture="black_white.png"),
}

FLAG_TEXTURES = {
    flag_value: ac.newTexture(TEXTURE_DIR + flag.texture)
    for flag_value, flag in FLAGS.items()
}
    
    
def acMain(ac_version):
    global flag_label, appWindow

    # Initialise app
    appWindow = ac.newApp(APP_NAME)
    ac.setSize(appWindow, WINDOW_WIDTH, WINDOW_HEIGHT)
    ac.drawBorder(appWindow, 0)
    ac.setBackgroundOpacity(appWindow, BACKGROUND_OPACITY)

    # Add flag label text widget
    flag_label = ac.addLabel(appWindow, "")
    ac.setPosition(flag_label, PADDING, HEADER_HEIGHT)
    
    return APP_NAME
    
def acUpdate(deltaT):
    global flag_label, appWindow, previous_flag_value

    ac.setBackgroundOpacity(appWindow, BACKGROUND_OPACITY)

    flag_value = info.graphics.flag
    if flag_value != previous_flag_value:
        if SHOW_FLAG_NAME:
            flag_name = FLAGS[flag_value].name
            ac.setText(flag_label, flag_name)

        texture_id = FLAG_TEXTURES[flag_value]
        ac.glQuadTextured(0, HEADER_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT - HEADER_HEIGHT, texture_id)

    previous_flag_value = flag_value
