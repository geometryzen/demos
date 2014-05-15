# browser gives access to the window object and the WindowAnimationRunner.
from browser import *

# We have to get the window here so that we can pass it to the WindowAnimationRunner.
w = window.open("", "", "height=400, width=600")

def tick(time):
    w.document.title = "Window Popup Demonstration. Press Esc to quit."
    w.document.body.innerHTML = '<h1>' + str(time) + '</h1>'

def terminate(time):
    # Keep on going (don't terminate).
    return False

def setUp():
    print "Hello!"
    print "When you would like to terminate the animation,"
    print "press Esc key with the popup window as focus."

def tearDown(e):
    w.close()
    print "Goodbye!"
    # If an exception is thrown it will be reported here, otherwise None.
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, w).start()
