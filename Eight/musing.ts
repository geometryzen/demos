function removeElementsByTagName(tagName) {
  var elements = document.getElementsByTagName(tagName);
  for (var i = elements.length - 1; i >= 0; i--) {
    var e = elements[i];
    e.parentNode.removeChild(e);
  }
}

class Workbench2D
{
  public canvas;
  public wnd;
  private sizer: EventListener;
  constructor(canvas: HTMLCanvasElement, wnd: Window)
  {
    this.canvas = canvas;
    this.wnd = wnd;
    function onWindowResize(event)
    {
      var width  = wnd.innerWidth;
      var height = wnd.innerHeight;
      canvas.width  = width;
      canvas.height = height;
    }
    this.sizer = onWindowResize;
  }
  setUp()
  {
    document.body.insertBefore(this.canvas, document.body.firstChild);
    this.wnd.addEventListener('resize', this.sizer, false);
    this.sizer(null);

  }
  tearDown()
  {
    this.wnd.removeEventListener('resize', this.sizer, false);
    removeElementsByTagName("canvas");
  }
}


var glwin = window.open("","","width=800,height=600")
glwin.document.body.style.backgroundColor = "080808"
glwin.document.body.style.overflow = "hidden"
glwin.document.title = "Visualizing Geometric Algebra with WebGL"

var canvas2D = glwin.document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
var workbench2D = new Workbench2D(canvas2D, glwin)
var space2D = new createjs.Stage(canvas2D, "", {})
space2D.autoClear = true

var font = "20px Helvetica"

var output = new createjs.Text(glwin.document.title + ". Hit Esc key to exit.", font, "white")
output.x = 100
output.y = 60
space2D.addChild(output)

var scene = new THREE.Scene()

var camera = new THREE.PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10.0, 9.0, 8.0)
camera.up.set(0,0,1)
camera.lookAt(scene.position)

var ambientLight = new THREE.AmbientLight(0x111111)
scene.add(ambientLight)

var pointLight = new THREE.PointLight(0xFFFFFF)
pointLight.position.set(20.0, 20.0, 20.0)
scene.add(pointLight)

var directionalLight = new THREE.DirectionalLight(0xFFFFFF)
directionalLight.position.set(0.0, 1.0, 0.0)
scene.add(directionalLight)

var renderer = new THREE.WebGLRenderer()
renderer.setClearColor(new THREE.Color(0x080808), 1.0)

function material(color, opacity, transparent) {
    return new THREE.MeshLambertMaterial({"color": color,"opacity": opacity,"transparent": transparent})
}

var mesh = new THREE.Mesh(new THREE.BoxGeometry(5, 0.1, 5), material(0x00FF00, 1.0, false))
mesh.position.set(0, -2, 0)
scene.add(mesh)

arrow = THREE.Mesh(THREE.ArrowGeometry(4.0), material(0xFFFF00, 1.0, False))
scene.add(arrow)

box = THREE.Mesh(THREE.BoxGeometry(1,2,3), material(0xFF0000, 0.25, False))
scene.add(box)
box.position.set(3,-3,3)

vortex = THREE.Mesh(THREE.VortexGeometry(4.0, 0.32, 0.04, 0.08, 0.3, 8, 12), material(0x00FFff, 0.3, False))
scene.add(vortex)

flat = THREE.Mesh(THREE.BoxGeometry(10.0,10.0,0.1), material(0x0000FF, 0.25, True))
scene.add(flat)

CartesianSpace(scene, renderer)

workbench3D = Workbench3D(renderer.domElement, renderer, camera, glwin)

tau = 2 * pi
omega = (tau / 20) / second
# A unit bivector rotating from k to i
B = BivectorE3(0.0, 0.0, 1.0)
# Just make sure that we really do have a unit bivector.
B = B / magnitude(B)

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()

def tick(t):
    time = t * second
    theta = omega * time
    # The rotor is defined to have a minus sign.
    rotor = exp(-B*theta.quantity/2.0)
    # Unfortunately, we have to use a minus sign to convert the rotor grade 2 components to the quaternion values.
    arrow.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    
    box.attitude = rotor
    box.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)

    vortex.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    flat.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    renderer.render(scene, camera)
    space2D.render()

def tearDown(e):
    workbench3D.tearDown()
    workbench2D.tearDown()
    glwin.close()
    if e:
        print "Error during animation: %s" % (e)
    else:
        print "Goodbye!"

WindowAnimationRunner(tick, None, setUp, tearDown, glwin).start()
