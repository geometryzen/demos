'''
Demonstration of opening a window and running it as an animation.
'''
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

# Construct 
browser.WindowAnimationRunner(tick, terminate, setUp, tearDown, win).start()
