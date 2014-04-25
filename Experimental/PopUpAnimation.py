'''
Demonstration of opening a window and running it as an animation.
'''
# The browser module provides access to the current window
# and the WindowAnimationRunner utility.
import browser

win = browser.window.open("","","width=600,height=600")

def tick(time):
    win.document.body.innerHTML = str(time)
    pass

def terminate(time):
    return time > 10

def setUp():
    pass

def tearDown():
    win.close()
    print "The window was closed."

# Notice the last argument is the window that we want to control.
# The Esc key is monitored and used to break out of the animation.
browser.WindowAnimationRunner(tick, terminate, setUp, tearDown, win).start()
