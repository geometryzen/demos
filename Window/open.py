from browser import window, WindowAnimationRunner

w = None

def tick(time):
    w.document.body.innerHTML = '<h1>' + str(time) + '</h1>'
    pass

def terminate(time):
    return False

def setUp():
    print "Press Esc key with this window in focus to termintate the animation."
    global w
    w = window.open("", "MyWindow", "height=400, width=600")
    # w.document.write("<h1>Hello</h1>")

def tearDown():
    print "Closing the window that was opened."
    w.close()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
