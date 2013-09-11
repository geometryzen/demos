# The purpose of this experiment is to see if the details of a general example can be reproduced using convenience functions.
# TODO: Allow material to be replaced so that the cylinder is visible without illumination.
from three import *
from geometry import CylinderBuilder
from browser import document, window, WindowAnimationRunner
from math import pi

scene = Scene()
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
renderer = WebGLRenderer({"antialias": True})
mesh = None
progressEnd = 10000
movement = Vector3(0.02, 0.02, 0.02)

def setUp():
    global mesh

    document.removeElementsByTagName('canvas')
    renderer.setClearColor(Color(0x080808), 1.0)

    container = document.getElementById("canvas-container")
    container.appendChild(renderer.domElement)

    camera.position.z = 100

    radiusTop = 20
    radiusBottom = 20
    height = 100
    radialSegments = 32
    heightSegments = 1
    openEnded = False
    material = MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3})
    mesh = CylinderBuilder().radiusTop(radiusTop).radiusBottom(radiusBottom).height(height).material(material).build()
    cylinder = mesh.geometry
    #cylinder = CylinderGeometry(radiusTop, radiusBottom, height, radialSegments, heightSegments, openEnded)

    print repr(cylinder)
    print "radiusTop:      " + str(cylinder.radiusTop)
    print "radiusBottom:   " + str(cylinder.radiusBottom)
    print "height:         " + str(cylinder.height)
    print "radialSegments: " + str(cylinder.radialSegments)
    print "heightSegments: " + str(cylinder.heightSegments)
    print "openEnded:      " + str(cylinder.openEnded)
    print cylinder

    #mesh = Mesh(cylinder, material)
    scene.add(mesh)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tick(elapsed):
    mesh.rotation += movement
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > progressEnd

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeElementsByTagName('canvas')

def onWindowResize(event):
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()