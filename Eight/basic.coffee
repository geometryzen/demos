eight = window.EIGHT

glwin = window.open "","","width=800,height=600"

glwin.document.body.style.backgroundColor = "202020"
glwin.document.body.style.overflow = "hidden"
glwin.document.title = "Visualizing Geometric Algebra with WebGL"

scene = eight.scene()

camera = eight.perspectiveCamera 45, 1.0, 0.1, 100

renderer = eight.webGLRenderer()

box = eight.mesh eight.boxGeometry()
scene.add box
box.position = eight.vectorE3 -1.0, -0.5, -5.0
prism = eight.mesh eight.prismGeometry()
scene.add prism
prism.position = eight.vectorE3 0.0, 0.0, -5.0

workbench3D = eight.workbench3D renderer.canvas, renderer, camera, glwin

setUp = ->
  workbench3D.setUp()
  monitor.start()

B = eight.bivectorE3 0, 0, 1
angle = 0

stats = new Stats()
stats.setMode 0
stats.domElement.style.position = 'absolute'
stats.domElement.style.left = '0px'
stats.domElement.style.top = '0px'
glwin.document.body.appendChild stats.domElement

tick = (t) ->
  stats.begin()
  # Klunky math until we get the operator overloading and GA carried over to JavaScript!
  c = eight.scalarE3 Math.cos angle/2
  s = eight.scalarE3 Math.sin angle/2
  R = c.sub B.mul s
  box.attitude = R
  prism.attitude = R

  renderer.render scene, camera
  angle += 0.01
  stats.end()

terminate = (t) -> false

tearDown = (e) ->
  monitor.stop()
  glwin.close()
  workbench3D.tearDown()
  scene.tearDown()
  if e
    console.log "Error during animation: #{e}"
  else
    console.log "Goodbye!"

runner = eight.windowAnimationRunner tick, terminate, setUp, tearDown, glwin

onContextLoss = ->
  runner.stop()
  renderer.onContextLoss()
  scene.onContextLoss()

onContextGain = (gl) ->
  scene.onContextGain gl
  renderer.onContextGain gl
  runner.start()

monitor = eight.webGLContextMonitor renderer.canvas, onContextLoss, onContextGain

onContextGain renderer.context
