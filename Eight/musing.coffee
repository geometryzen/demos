removeElementsByTagName = (doc, tagName) ->
  elements = doc.getElementsByTagName(tagName)
  for element in elements
    if element
      element.parentNode.removeChild(element)

class Workbench2D
  constructor: (canvas, wnd) ->
    this.canvas = canvas
    this.wnd = wnd
    onWindowResize = (event) ->
      width  = wnd.innerWidth
      height = wnd.innerHeight
      canvas.width  = width
      canvas.height = height
    this.sizer = onWindowResize

  setUp: () ->
    this.wnd.document.body.insertBefore(this.canvas, this.wnd.document.body.firstChild)
    this.wnd.addEventListener('resize', this.sizer, false)
    this.sizer(null)
    
  tearDown: () ->
    this.wnd.removeEventListener('resize', this.sizer, false)

class Workbench3D
  constructor: (canvas, renderer, camera, wnd) ->
    this.canvas = canvas;
    this.wnd = wnd;
    onWindowResize = (event) ->
      width  = wnd.innerWidth
      height = wnd.innerHeight
      renderer.setSize(width, height)
      camera.aspect = width / height
      camera.updateProjectionMatrix()
    this.sizer = onWindowResize

  setUp: () ->
    this.wnd.document.body.insertBefore(this.canvas, this.wnd.document.body.firstChild)
    this.wnd.addEventListener('resize', this.sizer, false)
    this.sizer(null)

  tearDown: () ->
    this.wnd.removeEventListener('resize', this.sizer, false)

glwin = window.open("","","width=800,height=600")
glwin.document.body.style.backgroundColor = "080808"
glwin.document.body.style.overflow = "hidden"
glwin.document.title = "Visualizing Geometric Algebra with WebGL"

canvas2D = glwin.document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = new Workbench2D(canvas2D, glwin)
space2D = new createjs.Stage(canvas2D, "", {})
space2D.autoClear = true

font = "20px Helvetica"

output = new createjs.Text(glwin.document.title + ". Hit Esc key to exit.", font, "white")
output.x = 100
output.y = 60
space2D.addChild(output)

scene = new THREE.Scene()

camera = new THREE.PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10.0, 9.0, 8.0)
camera.up.set(0,0,1)
camera.lookAt(scene.position)

ambientLight = new THREE.AmbientLight(0x111111)
scene.add(ambientLight)

pointLight = new THREE.PointLight(0xFFFFFF)
pointLight.position.set(20.0, 20.0, 20.0)
scene.add(pointLight)

directionalLight = new THREE.DirectionalLight(0xFFFFFF)
directionalLight.position.set(0.0, 1.0, 0.0)
scene.add(directionalLight)

renderer = new THREE.WebGLRenderer()
renderer.setClearColor(new THREE.Color(0x080808), 1.0)

material = (color, opacity, transparent) ->
    return new THREE.MeshLambertMaterial({"color": color,"opacity": opacity,"transparent": transparent})

mesh = new THREE.Mesh(new THREE.BoxGeometry(5, 0.1, 5), material(0x00FF00,1,false))
mesh.position.set(0, -2, 0)
scene.add(mesh)

arrow = new THREE.Mesh(new THREE.ArrowGeometry(4.0), material(0xFFFF00,1,false))
scene.add(arrow)

box = new THREE.Mesh(new THREE.BoxGeometry(1,2,3), material(0xFF0000, 0.25, false))
scene.add(box)
box.position.set(3,-3,3)

vortex = new THREE.Mesh(new THREE.VortexGeometry(4.0, 0.32, 0.04, 0.08, 0.3, 8, 12), material(0x00FFff, 0.3, false))
scene.add(vortex)

flat = new THREE.Mesh(new THREE.BoxGeometry(10.0,10.0,0.1), material(0x0000FF, 0.25, true))
scene.add(flat)


# CartesianSpace(scene, renderer)

workbench3D = new Workbench3D(renderer.domElement, renderer, camera, glwin)

tau = 2 * Math.PI
omega = (tau / 20)
# A unit bivector rotating from k to i
B = new blade.Euclidean3(0,0,0,0,0.0, 0.0, 1.0,0)
# Just make sure that we really do have a unit bivector.
B = B / B.norm()

setUp = () ->
    workbench2D.setUp()
    workbench3D.setUp()

tick = (time) ->
    theta = omega * time
    # The rotor is defined to have a minus sign.
    s = new blade.Euclidean3(Math.cos(theta/2),0,0,0,0,0,0,0)
    rotor = s - B * Math.sin(theta/2)
    # Unfortunately, we have to use a minus sign to convert the rotor grade 2 components to the quaternion values.
    arrow.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    
    # box.attitude = rotor
    box.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)

    vortex.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    flat.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    renderer.render(scene, camera)
    space2D.update()

terminate = (time) ->
  return false

tearDown = (e) ->
    workbench3D.tearDown()
    workbench2D.tearDown()
    removeElementsByTagName(glwin.document, "canvas")
    glwin.close()

eight.animationRunner(tick, terminate, setUp, tearDown, glwin).start()
