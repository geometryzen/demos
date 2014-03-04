# Under Construction
from browser import document, window, WindowAnimationRunner

screenX = 0
screenY = 0
clientX = 0
clientY = 0
button = 0

progressEnd = 10


def onDocumentKeyDown(event):
    if event.keyCode == 27:
        # TODO: Implement stop, pause, resume?
        war.stop()
        pass

def onDocumentMouseDown(event):
    event.preventDefault()
    global screenX, screenY, clientX, clientY
    screenX = event.screenX
    screenY = event.screenY
    clientX = event.clientX
    clientY = event.clientY
    button = event.button
    if event.altKey:
        print "ALT"
    if event.ctrlKey:
        print "CTRL"
    if event.shiftKey:
        print "SHIFT"
    event.stopPropagation()
    event.stopImmediatePropagation()
    print {"event.cancelable": event.cancelable}
    print {"event.bubbles": event.bubbles}
    print {"event.defaultPrevented": event.defaultPrevented}

def setUp():
    print "Hello!"
    print "This program demonstrates the use of the Mouse."        
    # print "Press ESC to terminate."
    print "This program will 'self-terminate' in "+str(progressEnd/1000)+" seconds!"
    # document.addEventListener('keydown', onDocumentKeyDown, False)
    document.addEventListener('mousedown', onDocumentMouseDown, False)

def tick(elapsed):
    pass
    
def terminate(elapsed):
    return elapsed > progressEnd
        
def tearDown():
    # document.removeEventListener('keydown', onDocumentKeyDown, False)
    document.removeEventListener('mousedown', onDocumentMouseDown, False)
    print "Goodbye."

war = WindowAnimationRunner(tick, terminate, setUp, tearDown)

war.start()