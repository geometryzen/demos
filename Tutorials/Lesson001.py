'''
This lesson demonstrates the structure required to support animation.
It will print to the Output area to show you what is happening.
We don't actually render anything in 3D until the next lesson.
'''
from browser import WindowAnimationRunner

frames = 0
elapsed = 0.0

# The tick function is called repeatedly with a time parameter (in seconds).
# You will be expected to move objects in your animation and then render them in this function.
def tick(time):
    global elapsed, frames
    elapsed = time
    frames += 1
#   print "It's time to move and render. The time is now " + str(time)

# The terminate function is called repeatedly with a time parameter (in seconds).
# It is used by the animation runner to determine whether the animation should end. 
def terminate(time):
    done = time > 1
#   print "The time is " + str(time) + ". Are we done yet? " + str(done)
    return done

# The setUp function is called once at the beginning of the animation.
def setUp():
    pass

# The tearDown function is called once at the end of the animation.
def tearDown(e):
    print frames / elapsed
    if e:
        print e

# The animation starts when the start method is caled.
war = WindowAnimationRunner(tick, terminate, setUp, tearDown)

war.start()
