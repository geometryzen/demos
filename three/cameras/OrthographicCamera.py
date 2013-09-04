from three import *
from browser import *
from math import cos, sin, floor
from time import time
from random import random

useLargeCanvas = True

# Global variables
camera = OrthographicCamera(-1, 1, 1, -1, -500, 1000)
camera.position.x = 200
camera.position.y = 100
camera.position.z = 200

renderer = WebGLRenderer({"antialias": True})
renderer.setClearColor(Color(0xFFFFFF), 1.0)
scene = Scene()
view = document.getElementById("view")
progressEnd = 6000

def onWindowResize(event):
    if (useLargeCanvas):
        halfW = window.innerWidth / 2
        halfH = window.innerHeight / 2
        
        camera.left = -halfW
        camera.right = halfW
        camera.top = halfH
        camera.bottom = -halfH
        camera.updateProjectionMatrix()
        renderer.setSize(window.innerWidth, window.innerHeight)
    else:
        container = document.getElementById("canvas-container")
        halfW = container.clientWidth / 2
        halfH = container.clientHeight / 2
        
        camera.left = -halfW
        camera.right = halfW
        camera.top = halfH
        camera.bottom = -halfH
        camera.updateProjectionMatrix()
        renderer.setSize(container.clientWidth, container.clientHeight)
    
def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)

def setUp():
    print "Hello!"
    print "This example will end automatically in "+str(progressEnd/1000)+" seconds."
    discardCanvases()
    if (useLargeCanvas):
        document.body.insertBefore(renderer.domElement, document.body.firstChild)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(renderer.domElement)

    # Grid
    size = 500
    step = 50
    geometry = Geometry()
    for i in range(-size, size+step, step):
        geometry.vertices.append(Vector3(-size, 0, i))
        geometry.vertices.append(Vector3(+size, 0, i))
        geometry.vertices.append(Vector3( i, 0, -size))
        geometry.vertices.append(Vector3( i, 0, +size))
        
    material = LineBasicMaterial({"color":0x000000,"opacity":0.2})
    
    line = Line(geometry, material)
    line.type = LinePieces
    scene.add(line)
    
    # Cubes
    geometry = CubeGeometry(50, 50, 50)
    material = MeshLambertMaterial({"color":0xFFFFFF,"shading":FlatShading, "overdraw":True})
    for i in range(0, 100):
        cube = Mesh(geometry, material)
        cube.scale.y = floor(random() * 2 + 1)
        cube.position.x = floor((random() * 1000 - 500) / 50) * 50 + 25
        cube.position.y = (cube.scale.y * 50) / 2
        cube.position.z = floor((random() * 1000 - 500) / 50) * 50 + 25
        scene.add(cube)
        
    # Lights
    ambientLight = AmbientLight(random() * 0x10)
    scene.add(ambientLight)
    
    directionalLight = DirectionalLight(random() * 0xFFFFFF)
    directionalLight.position.x = random() - 0.5
    directionalLight.position.y = random() - 0.5
    directionalLight.position.z = random() - 0.5
    directionalLight.position.normalize()
    scene.add(directionalLight)
    
    directionalLight = DirectionalLight(random() * 0xFFFFFF)
    directionalLight.position.x = random() - 0.5
    directionalLight.position.y = random() - 0.5
    directionalLight.position.z = random() - 0.5
    directionalLight.position.normalize()
    scene.add(directionalLight)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tick(elapsed):
    theta = time() * 0.1
    
    camera.position.x = cos(theta) * 200
    camera.position.z = sin(theta) * 200
    camera.lookAt(scene.position)
    
    renderer.render(scene, camera)

def terminate(elapsed):
    return elapsed > progressEnd

def tearDown():
    discardCanvases()
    print "Goodbye!"

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()