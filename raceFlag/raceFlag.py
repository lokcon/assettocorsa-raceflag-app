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
BACKGROUND_OPACITY = 0.3

# Generate flags
Flag = collections.namedtuple("Flag", ["name", "texture"])
FLAGS = {
    AC_NO_FLAG:        Flag(name="No flag",   texture="empty.png"),
    AC_BLUE_FLAG:      Flag(name="Blue",      texture="blue.png"),
    AC_YELLOW_FLAG:    Flag(name="Yellow",    texture="yellow.png"),
    AC_BLACK_FLAG:     Flag(name="Black",     texture="black.png"),
    AC_WHITE_FLAG:     Flag(name="White",     texture="white.png"),
    AC_CHECKERED_FLAG: Flag(name="Checkered", texture="chequered.png"),
    AC_PENALTY_FLAG:   Flag(name="Penalty",   texture="black_white.png"),
}

# Global variables
appWindow = None
flag_textures = None
    
    
def acMain(ac_version):
    global appWindow, flag_textures

    # Initialise app
    appWindow = ac.newApp(APP_NAME)
    ac.setSize(appWindow, WINDOW_WIDTH, WINDOW_HEIGHT)
    ac.setIconPosition(appWindow, 0, -999999)
    ac.setTitle(appWindow, " ")
    ac.drawBorder(appWindow, 0)
    ac.setBackgroundOpacity(appWindow, BACKGROUND_OPACITY)
    ac.addRenderCallback(appWindow, onWindowRender)

    # Load flag textures
    flag_textures = {
        flag_value: ac.newTexture(TEXTURE_DIR + flag.texture)
        for flag_value, flag in FLAGS.items()
    }
    
    return APP_NAME
    
def acUpdate(deltaT):
    global appWindow

    ac.setBackgroundOpacity(appWindow, BACKGROUND_OPACITY)


def onWindowRender(deltaT):
    global flag_textures

    flag_value = info.graphics.flag
    texture_id = flag_textures[flag_value]
    ac.glColor4f(1.0, 1.0, 1.0, BACKGROUND_OPACITY)
    ac.glQuadTextured(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, texture_id)

