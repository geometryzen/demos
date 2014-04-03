from browser import window, WindowAnimationRunner

#window.open("http://www.geometryzen.org")
w = window.open("https://www.google.com","_blank")

def tick():
    pass

def terminate(time):
    return False

def setUp():
    pass

def tearDown():
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
