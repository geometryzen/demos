from browser import window, WindowAnimationRunner

#window.open("http://www.geometryzen.org")
w = window.open("https://www.google.com","_blank")

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
