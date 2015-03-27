function removeElementsByTagName(doc: Document, tagName: string) {
  var elements = doc.getElementsByTagName(tagName);
  for (var i = elements.length - 1; i >= 0; i--) {
    var e = elements[i];
    e.parentNode.removeChild(e);
  }
}

class Visual<T extends THREE.Geometry>
{
  public geometry: T;
  public material: THREE.MeshLambertMaterial;
  public mesh: THREE.Mesh;
  constructor(geometry: T, color: number, opacity: number = 1.0, transparent: boolean = false)
  {
    this.geometry = geometry;
    this.material = new THREE.MeshLambertMaterial({"color": color,"opacity": opacity,"transparent": transparent});
    this.mesh = new THREE.Mesh(this.geometry, this.material);
  }
  set position(p: blade.Euclidean3)
  {
    this.mesh.position.set(p.x, p.y, p.z);
  }
  set attitude(rotor: blade.Euclidean3)
  {
    this.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
  }
  
  set scale(value: number)
  {
    this.mesh.scale = new THREE.Vector3(value, value, value);
  }
  
  set color(color: THREE.Color)
  {
    this.material.color = color;
  }
}

class Arrow extends Visual<THREE.ArrowGeometry>
{
  constructor(scale: number, color: number, opacity: number = 1.0, transparent: boolean = false)
  {
    super(new THREE.ArrowGeometry(scale), color, opacity, transparent);
  }
}

class Box extends Visual<THREE.BoxGeometry>
{
  constructor(width: number, height: number, depth: number, color: number, opacity: number = 1.0, transparent: boolean = false)
  {
    super(new THREE.BoxGeometry(width, height, depth), color, opacity, transparent);
  }
}

class Vortex extends Visual<THREE.VortexGeometry>
{
  constructor(scale: number, color: number, opacity: number = 1.0, transparent: boolean = false)
  {
    super(new THREE.VortexGeometry(4.0, 0.32, 0.04, 0.08, 0.3, 8, 12), color, opacity, transparent);
  }
}

class Workbench2D
{
  public canvas: HTMLCanvasElement;
  public wnd: Window;
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
    this.wnd.document.body.insertBefore(this.canvas, this.wnd.document.body.firstChild);
    this.wnd.addEventListener('resize', this.sizer, false);
    this.sizer(null);

  }
  tearDown()
  {
    this.wnd.removeEventListener('resize', this.sizer, false);
    removeElementsByTagName(this.wnd.document, "canvas");
  }
}

class Workbench3D
{
  public canvas: HTMLCanvasElement;
  public wnd: Window;
  private sizer: EventListener;
  constructor(canvas: HTMLCanvasElement, renderer: THREE.WebGLRenderer, camera: THREE.PerspectiveCamera, wnd: Window)
  {
    this.canvas = canvas;
    this.wnd = wnd;
    function onWindowResize(event)
    {
      var width  = wnd.innerWidth;
      var height = wnd.innerHeight;
      renderer.setSize(width, height);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
    }
    this.sizer = onWindowResize;
  }
  setUp()
  {
    this.wnd.document.body.insertBefore(this.canvas, this.wnd.document.body.firstChild);
    this.wnd.addEventListener('resize', this.sizer, false);
    this.sizer(null);

  }
  tearDown()
  {
    this.wnd.removeEventListener('resize', this.sizer, false);
    removeElementsByTagName(this.wnd.document, "canvas");
  }
}


var glwin: Window = window.open("","","width=800,height=600");
glwin.document.body.style.backgroundColor = "080808";
glwin.document.body.style.overflow = "hidden";
glwin.document.title = "Visualizing Geometric Algebra with WebGL";

var canvas2D = glwin.document.createElement("canvas");
canvas2D.style.position = "absolute";
canvas2D.style.top = "0px";
canvas2D.style.left = "0px";
var workbench2D = new Workbench2D(canvas2D, glwin);
var space2D = new createjs.Stage(canvas2D, "", {});
space2D.autoClear = true;

var font = "20px Helvetica";

var output = new createjs.Text(glwin.document.title + ". Hit Esc key to exit.", font, "white");
output.x = 100;
output.y = 60;
space2D.addChild(output);

var scene = new THREE.Scene();

var camera = new THREE.PerspectiveCamera(45, 1.0, 0.1, 10000);
camera.position.set(10.0, 9.0, 8.0);
camera.up.set(0,0,1);
camera.lookAt(scene.position);

var ambientLight = new THREE.AmbientLight(0x111111);
scene.add(ambientLight);

var pointLight = new THREE.PointLight(0xFFFFFF);
pointLight.position.set(20.0, 20.0, 20.0);
scene.add(pointLight);

var directionalLight = new THREE.DirectionalLight(0xFFFFFF);
directionalLight.position.set(0.0, 1.0, 0.0);
scene.add(directionalLight);

var renderer = new THREE.WebGLRenderer()
renderer.setClearColor(new THREE.Color(0x080808), 1.0)

var mono = new Box(5.0, 0.1, 5.0, 0x00FF00);
mono.mesh.position.set(0, -2, 0);
scene.add(mono.mesh);

var arrow = new Arrow(4.0, 0xFFFF00);
scene.add(arrow.mesh);

var box = new Box(1.0, 2.0, 3.0, 0xFF0000, 0.25, false);
scene.add(box.mesh);
box.mesh.position.set(3,-3,3);

var vortex = new Vortex(1.0, 0x00FFff, 0.3);
scene.add(vortex.mesh)

var flat = new Box(10.0,10.0,0.1, 0x0000FF, 0.25, true);
scene.add(flat.mesh);

//CartesianSpace(scene, renderer)

var workbench3D = new Workbench3D(renderer.domElement, renderer, camera, glwin);

var tau = 2 * Math.PI;
var omega = (tau / 20);
// A unit bivector rotating from k to i
var B: any = new blade.Euclidean3(0,0,0,0,0.0, 0.0, 1.0,0);
// Just make sure that we really do have a unit bivector.
B = B / B.norm();

function setUp() {
    workbench2D.setUp();
    workbench3D.setUp();
}

function tick(time: number) {
    var theta = omega * time;
    // The rotor is defined to have a minus sign.
    var s: any = new blade.Euclidean3(Math.cos(theta/2),0,0,0,0,0,0,0);
    var rotor: any = s - B * Math.sin(theta/2);

    arrow.attitude = rotor;
    box.attitude = rotor;
    flat.attitude = rotor;
    vortex.attitude = rotor;

    renderer.render(scene, camera);
    space2D.update();
}

function terminate(time: number) {
  return false;
}

function tearDown(e) {
    workbench3D.tearDown();
    workbench2D.tearDown();
    glwin.close();
}

eight.animationRunner(tick, terminate, setUp, tearDown, glwin).start();
