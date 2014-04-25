'''
Demonstration of opening a window and running it as an animation.
'''
# The browser module provides access to the current window
# and the WindowAnimationRunner utility.
import browser

win = browser.window.open("","","width=600,height=600")

def tick(time):
    # raise NameError('Hello')
    win.document.body.innerHTML = str(time)
    pass

def terminate(time):
    print "Are we done yet?" + str(time)
    return time > 4

def setUp():
    print "Off we go!"
    pass

def tearDown(e):
    win.close()
    print "The window was closed. " + str(e)

# Notice the last (optional) argument is the window that we want to control.
# The Esc key is monitored and used to break out of the animation.
browser.WindowAnimationRunner(tick, terminate, setUp, tearDown, win).start()
