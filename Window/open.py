from browser import window, WindowAnimationRunner

# We have to get the window here so that we can pass it to the WindowAnimationRunner
w = window.open("", "", "height=400, width=600")

def tick(time):
    w.document.body.innerHTML = '<h1>' + str(time) + '</h1>'
    pass

def terminate(time):
    # Keep on going...
    return False

def setUp():
    print "Press Esc key with the popup window as focus to termintate the animation."

def tearDown(e):
    w.close()
    # If an exception is thrown it will be reported here.
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, w).start()
