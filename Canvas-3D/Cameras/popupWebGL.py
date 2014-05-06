from browser import window, WindowAnimationRunner
from math import cos, sin, floor
from random import random

THREE = window.THREE

glwin = window.open("","","width=1200,height=800")

# Global variables
camera = THREE.OrthographicCamera(-1.0, 1.0, 1.0, -1.0, -500.0, 1000.0)
camera.position.x = 200.0
camera.position.y = 100.0
camera.position.z = 200.0

renderer = THREE.WebGLRenderer({"antialias": True})
renderer.setClearColor(THREE.Color(0xFFFFFF), 1.0)
scene = THREE.Scene()
progressEnd = 10

def onWindowResize(event):
    halfW = glwin.innerWidth / 2
    halfH = glwin.innerHeight / 2
        
    camera.left = -halfW
    camera.right = halfW
    camera.top = halfH
    camera.bottom = -halfH
    camera.updateProjectionMatrix()
    renderer.setSize(glwin.innerWidth, glwin.innerHeight)
    
def setUp():
    print "Hello!"
    print "This example will end automatically in "+str(progressEnd)+" seconds."
    # A bit surprising that this works given two different documents.
    glwin.document.body.insertBefore(renderer.domElement, glwin.document.body.firstChild)

    # Grid
    size = 500
    step = 50
    geometry = THREE.Geometry()
    for i in range(-size, size+step, step):
        geometry.vertices.append(THREE.Vector3(float(-size), 0.0, float(i)))
        geometry.vertices.append(THREE.Vector3(float(+size), 0.0, float(i)))
        geometry.vertices.append(THREE.Vector3( float(i), 0.0, float(-size)))
        geometry.vertices.append(THREE.Vector3( float(i), 0.0, float(+size)))
        
    material = THREE.LineBasicMaterial({"color":0x000000,"opacity":0.2})
    
    line = THREE.Line(geometry, material)
    line.type = THREE.LinePieces
    scene.add(line)
    
    # Cubes
    geometry = THREE.CubeGeometry(50, 50, 50)
    material = THREE.MeshLambertMaterial({"color":0xFFFFFF,"shading":THREE.FlatShading, "overdraw":True})
    for i in range(0, 100):
        cube = THREE.Mesh(geometry, material)
        cube.scale.y = floor(random() * 2 + 1)
        cube.position.x = floor((random() * 1000 - 500) / 50) * 50 + 25
        cube.position.y = (cube.scale.y * 50) / 2
        cube.position.z = floor((random() * 1000 - 500) / 50) * 50 + 25
        scene.add(cube)
        
    # Lights
    ambientLight = THREE.AmbientLight(random() * 0x10)
    scene.add(ambientLight)
    
    directionalLight = THREE.DirectionalLight(random() * 0xFFFFFF)
    directionalLight.position.x = random() - 0.5
    directionalLight.position.y = random() - 0.5
    directionalLight.position.z = random() - 0.5
    directionalLight.position.normalize()
    scene.add(directionalLight)
    
    directionalLight = THREE.DirectionalLight(random() * 0xFFFFFF)
    directionalLight.position.x = random() - 0.5
    directionalLight.position.y = random() - 0.5
    directionalLight.position.z = random() - 0.5
    directionalLight.position.normalize()
    scene.add(directionalLight)

    glwin.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tick(t):
    theta = t * 0.1
    
    camera.position.x = cos(theta) * 200
    camera.position.z = sin(theta) * 200
    camera.lookAt(scene.position)
    
    renderer.render(scene, camera)

def terminate(t):
    return t > progressEnd

def tearDown(e):
    glwin.close()
    print "Goodbye!"
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, glwin).start()