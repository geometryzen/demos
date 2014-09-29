from browser import window;

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 800

s = "width=%s, height=%s" % (WINDOW_WIDTH, WINDOW_HEIGHT)

print s

popUp = window.open("","","width=%1, height=%2" % (WINDOW_WIDTH, WINDOW_HEIGHT))