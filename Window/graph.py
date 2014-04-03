from browser import window, WindowAnimationRunner

w = None

def tick(time):
    pass

def terminate(time):
    return False

def setUp():
    print "Press Esc key with this window as focus to termintate the animation."
    global w
    w = window.open("", "", "height=400, width=600")
    w.document.body.innerHTML = '<h1>' + '</h1>'

def tearDown():
    w.close()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()

