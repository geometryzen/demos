from browser import window, WindowAnimationRunner

w = None
#w.document.write("Hello")

def tick(time):
    pass

def terminate(time):
    return False

def setUp():
    global w
    w = window.open("", "MyWindow", "height=400, width=600")
    print w.document
    w.document.body.innerHTML = '''
<h1>Hello!</h1>
'''

def tearDown():
    print "Closing the window that was opened."
    w.close()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
