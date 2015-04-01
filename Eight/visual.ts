// This program is under development.
var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

log("Hello!");
log(visual.VERSION);

function removeElementsByTagName(doc: Document, tagName: string) {
  var elements = doc.getElementsByTagName(tagName);
  for (var i = elements.length - 1; i >= 0; i--) {
    var e = elements[i];
    e.parentNode.removeChild(e);
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
  public controls;

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

    this.controls = new TrackballControls( this.camera, wnd );
    
    this.renderer.setClearColor(new THREE.Color(0x080808), 1.0)
    this.workbench3D = new Workbench3D(this.renderer.domElement, this.renderer, this.camera, this.controls, wnd);
    
    this.canvas2D = wnd.document.createElement("canvas");

    this.canvas2D.style.position = "absolute";
    this.canvas2D.style.top = "0px";
    this.canvas2D.style.left = "0px";
    
    this.workbench2D = new Workbench2D(this.canvas2D, wnd);
    this.space2D = new createjs.Stage(this.canvas2D, "", {});
    this.space2D.autoClear = true;

    this.controls.rotateSpeed = 1.0;
    this.controls.zoomSpeed = 1.2;
    this.controls.panSpeed = 0.8;

    this.controls.noZoom = false;
    this.controls.noPan = false;

    this.controls.staticMoving = true;
    this.controls.dynamicDampingFactor = 0.3;

    this.controls.keys = [ 65, 83, 68 ];
    
    function render()
    {
      
    }

    this.controls.addEventListener( 'change', render );
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
    this.controls.update();
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
  constructor(canvas: HTMLCanvasElement, renderer: THREE.WebGLRenderer, camera: THREE.PerspectiveCamera, controls, wnd: Window)
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
      controls.handleResize();
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
output.x = 100; output.y = 60;
viz.space2D.addChild(output);

var mono = new visual.Box(5.0, 0.1, 5.0, 0x00FF00);
mono.mesh.position.set(0, -2, 0);
viz.add(mono.mesh);

var arrow = new visual.Arrow(4.0, 0xFFFF00);
viz.add(arrow.mesh);

var box = new visual.Box(1.0, 2.0, 3.0, 0xFF0000, 0.25, false);
viz.add(box.mesh);
box.mesh.position.set(3,-3,3);

var vortex = new visual.Vortex(1.0, 0x00FFFF, 0.3);
viz.add(vortex.mesh)

var flat = new visual.Box(10.0,10.0,0.1, 0x0000FF, 0.25, true);
viz.add(flat.mesh);

var tau = 2 * Math.PI;
var omega = (tau / 10);
// A unit bivector rotating from k to i
var B: any = new blade.Euclidean3(0, 0, 0, 0, 0, 0, 1, 0);
// Just make sure that we really do have a unit bivector.
B = B / B.norm();

function setUp() { viz.setUp(); }

function tick(time: number) {
    var theta = omega * time;
    var s: any = new blade.Euclidean3(Math.cos(theta/2), 0, 0, 0, 0, 0, 0, 0);
    var rotor: any = s - B * Math.sin(theta/2);

      arrow.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
      box.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
      flat.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
      vortex.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);

    viz.update();
}

function terminate(time: number) { return false; }

function tearDown(e: Error) { viz.tearDown(); popUp.close(); }

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();
