from browser import window, WindowAnimationRunner

#window.open("http://www.geometryzen.org")
w = window.open("","", "height=200, width=100")

#w.document.write("Hello")

def tick(time):
    pass

def terminate(time):
    return False

def setUp():
    pass

def tearDown():
    print "Closing the window that was opened."
    w.close()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
