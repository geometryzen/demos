function removeElementsByTagName(doc: Document, tagName: string) {
  var elements = doc.getElementsByTagName(tagName);
  for (var i = elements.length - 1; i >= 0; i--) {
    var e = elements[i];
    e.parentNode.removeChild(e);
  }
}

/**
 * Visual provides the common behavior for all Mesh (Geometry, Material) objects.
 */
class VisualElement<T extends THREE.Geometry>
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
  get attitude()
  {
    var q: THREE.Quaternion = this.mesh.quaternion;
    return new blade.Euclidean3(q.w, 0, 0, 0, -q.z, -q.x, -q.y, 0);
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

class Arrow extends VisualElement<THREE.ArrowGeometry>
{
  constructor(scale: number, color: number, opacity: number = 1.0, transparent: boolean = false)
  {
    super(new THREE.ArrowGeometry(scale), color, opacity, transparent);
  }
}

class Box extends VisualElement<THREE.BoxGeometry>
{
  constructor(width: number, height: number, depth: number, color: number, opacity: number = 1.0, transparent: boolean = false)
  {
    super(new THREE.BoxGeometry(width, height, depth), color, opacity, transparent);
  }
}

class Vortex extends VisualElement<THREE.VortexGeometry>
{
  constructor(scale: number, color: number, opacity: number = 1.0, transparent: boolean = false)
  {
    super(new THREE.VortexGeometry(4.0, 0.32, 0.04, 0.08, 0.3, 8, 12), color, opacity, transparent);
  }
}

class Visual
{
  public scene: THREE.Scene = new THREE.Scene();
  public camera: THREE.PerspectiveCamera = new THREE.PerspectiveCamera(45, 1.0, 0.1, 10000);
  public renderer: THREE.WebGLRenderer = new THREE.WebGLRenderer();
  public workbench3D: Workbench3D;
  public canvas2D: HTMLCanvasElement;
  public workbench2D: Workbench2D;
  public space2D: createjs.Stage;

  constructor(wnd: Window)
  {
    var ambientLight = new THREE.AmbientLight(0x111111);
    this.scene.add(ambientLight);

    var pointLight = new THREE.PointLight(0xFFFFFF);
    pointLight.position.set(20.0, 20.0, 20.0);
    this.scene.add(pointLight);

    var directionalLight = new THREE.DirectionalLight(0xFFFFFF);
    directionalLight.position.set(0.0, 1.0, 0.0);
    this.scene.add(directionalLight);

    this.camera.position.set(10.0, 9.0, 8.0);
    this.camera.up.set(0,0,1);
    this.camera.lookAt(this.scene.position);
    
    this.renderer.setClearColor(new THREE.Color(0x080808), 1.0)
    this.workbench3D = new Workbench3D(this.renderer.domElement, this.renderer, this.camera, wnd);
    
    this.canvas2D = wnd.document.createElement("canvas");

    this.canvas2D.style.position = "absolute";
    this.canvas2D.style.top = "0px";
    this.canvas2D.style.left = "0px";
    
    this.workbench2D = new Workbench2D(this.canvas2D, wnd);
    this.space2D = new createjs.Stage(this.canvas2D, "", {});
    this.space2D.autoClear = true;
  }
  add(object: THREE.Object3D)
  {
    this.scene.add(object);
  }
  setUp()
  {
    this.workbench3D.setUp();
    this.workbench2D.setUp();
  }
  tearDown()
  {
    this.workbench3D.tearDown();
    this.workbench2D.tearDown();
  }
  update()
  {
    this.renderer.render(this.scene, this.camera);
    this.space2D.update();
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

var popUp: Window = window.open("","","width=800,height=600");
popUp.document.body.style.backgroundColor = "080808";
popUp.document.body.style.overflow = "hidden";
popUp.document.title = "Visualizing Geometric Algebra with WebGL";

var viz = new Visual(popUp);

var output = new createjs.Text(popUp.document.title + ". Hit Esc key to exit.", "20px Helvetica", "white");
output.x = 100;
output.y = 60;
viz.space2D.addChild(output);

var mono = new Box(5.0, 0.1, 5.0, 0x00FF00);
mono.mesh.position.set(0, -2, 0);
viz.add(mono.mesh);

var arrow = new Arrow(4.0, 0xFFFF00);
viz.add(arrow.mesh);

var box = new Box(1.0, 2.0, 3.0, 0xFF0000, 0.25, false);
viz.add(box.mesh);
box.mesh.position.set(3,-3,3);

var vortex = new Vortex(1.0, 0x00FFff, 0.3);
viz.add(vortex.mesh)

var flat = new Box(10.0,10.0,0.1, 0x0000FF, 0.25, true);
viz.add(flat.mesh);

var tau = 2 * Math.PI;
var omega = (tau / 20);
// A unit bivector rotating from k to i
var B: any = new blade.Euclidean3(0, 0, 0, 0, 0, 0, 1, 0);
// Just make sure that we really do have a unit bivector.
B = B / B.norm();

function setUp() { viz.setUp(); }

function tick(time: number) {
    var theta = omega * time;
    var s: any = new blade.Euclidean3(Math.cos(theta/2), 0, 0, 0, 0, 0, 0, 0);
    var rotor: any = s - B * Math.sin(theta/2);

    arrow.attitude = rotor;
    box.attitude = rotor;
    flat.attitude = rotor;
    vortex.attitude = rotor;

    viz.update();
}

function terminate(time: number) { return false; }

function tearDown(e) { viz.tearDown(); popUp.close(); }

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();
