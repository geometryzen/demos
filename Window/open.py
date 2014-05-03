from browser import window, WindowAnimationRunner

# We have to get the window here so that we can pass it to the WindowAnimationRunner
w = window.open("", "", "height=400, width=600")

def tick(time):
    w.document.body.innerHTML = '<h1>' + str(time) + '</h1>'
    pass

def terminate(time):
    return False

def setUp():
    print "Press Esc key with this window as focus to termintate the animation."
    global w

    # w.document.write("<h1>Hello</h1>")

def tearDown(e):
    w.close()
    print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, w).start()
