import browser

win = browser.window.open("","","width=415,height=400")

def tick(time):
    pass

def terminate(time):
    return time > 10

def setUp():
    pass

def tearDown():
    win.close()

WindowAnimationRunner(tick, terminate, setUp, tearDown, win).start()
