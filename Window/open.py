from browser import window, WindowAnimationRunner

w = None
#w.document.write("Hello")

def tick(time):
    pass

def terminate(time):
    return False

def setUp():
    global w
    w = window.open("","", "height=400, width=600")

def tearDown():
    print "Closing the window that was opened."
    w.close()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
