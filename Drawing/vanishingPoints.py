from browser import window;

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 800

s = "width={0}, height={1}".format(WINDOW_WIDTH, WINDOW_HEIGHT)

print s

popUp = window.open("","","width=%s, height=%s" % (WINDOW_WIDTH, WINDOW_HEIGHT))