from browser import window;
from workbench import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

popUp = window.open("","","width=%s, height=%s" % (WINDOW_WIDTH, WINDOW_HEIGHT))

WindowAnimationRunner()