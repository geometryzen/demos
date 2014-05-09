from three import *
from browser import *
from workbench import *
from random import random
from math import *

# global timeOut allows us to terminate the program gracefully on time or Esc key.
timeOut = 300
maxSteerForce = 0.1

class Bird:
    def __init__(self):
        self.position = VectorE3(random() - 0.5, random() - 0.5, random() - 0.5) * 400.0
        self.velocity = VectorE3(random() - 0.5, random() - 0.5, random() - 0.5) * 2.0
        self.phase = 0.0

        self._acceleration = VectorE3(0.0, 0.0, 0.0)
        self._avoidWalls = False
        self._width  = 500.0
        self._height = 500.0
        self._depth  = 500.0
        self._goal = None
        self._neighborhoodRadius = 100.0
        self._maxSpeed = 4.0

    def setAvoidWalls(self, avoidWalls):
        self._avoidWalls = avoidWalls

    def setWorldSize(self, width, height, depth):
        self._width  = width
        self._height = height
        self._depth  = depth
        
    def run(self, birds):
        if self._avoidWalls:
            vector = VectorE3(0.0, 0.0, 0.0)

            vector.set(-self._width, self.position.y, self.position.z)
            vector = self.avoid(vector)
            vector.multiplyScalar(5.0)
            self._acceleration.add(vector)

            vector.set(+self._width, self.position.y, self.position.z)
            vector = self.avoid(vector)
            vector.multiplyScalar(5.0)
            self._acceleration.add(vector)

            vector.set(self.position.x, -self._height, self.position.z)
            vector = self.avoid(vector)
            vector.multiplyScalar(5.0)
            self._acceleration.add(vector)

            vector.set(self.position.x, +self._height, self.position.z)
            vector = self.avoid(vector)
            vector.multiplyScalar(5.0)
            self._acceleration.add(vector)

            vector.set(self.position.x, self.position.y, -self._depth)
            vector = self.avoid(vector)
            vector.multiplyScalar(5.0)
            self._acceleration.add(vector)

            vector.set(self.position.x, self.position.y, +self._depth)
            vector = self.avoid(vector)
            vector.multiplyScalar(5.0)
            self._acceleration.add(vector)            
        else:
            pass
        if random() > 0.5:
            self.flock(birds)
        self.move()
            
    def flock(self, birds):
        if self._goal:
            self._acceleration.add(self.reach(self._goal, 0.005))
        self._acceleration.add(self.alignment(birds))
        self._acceleration.add(self.cohesion(birds))
        self._acceleration.add(self.separation(birds))
    
    def move(self):
        self.velocity.add(self._acceleration)
        speed = self.velocity.magnitude()
        if speed > self._maxSpeed:
            self.velocity.divideScalar(speed / self._maxSpeed)
        self.position.add(self.velocity)
        self._acceleration.set(0.0, 0.0, 0.0)
    
    def avoid(self, target):
        steer = VectorE3(0.0, 0.0, 0.0)
        steer.copy(self.position)
        steer.sub(target)
        steer.multiplyScalar(1.0 / self.position.distanceToSquared(target))
        return steer
    
    def alignment(self, birds):
        velSum = VectorE3(0.0, 0.0, 0.0)
        count = 0
        for i in range(0, len(birds)):
            if random() > 0.6:
                pass
            else:
                bird = birds[i]
                distance = bird.position.distanceTo(self.position)
                if distance > 0.0 and distance <= self._neighborhoodRadius:
                    velSum.add(bird.velocity)
                    count += 1
        if count > 0:
            velSum.divideScalar(float(count))
            a = velSum.magnitude()
            if a > maxSteerForce:
                velSum.divideScalar(a / maxSteerForce)
        return velSum
    
    def cohesion(self, birds):
        posSum = VectorE3(0.0, 0.0, 0.0)
        steer = VectorE3(0.0, 0.0, 0.0)
        count = 0
        for i in range(0, len(birds)):
            if random() > 0.6:
                pass
            else:
                bird = birds[i]
                distance = bird.position.distanceTo(self.position)
                if distance > 0.0 and distance <= self._neighborhoodRadius:
                    posSum.add(bird.position)
                    count += 1;
        if count > 0:
            posSum.divideScalar(float(count))
            
        steer = posSum - self.position
        f = steer.magnitude()
        if f > maxSteerForce:
            steer.divideScalar(f / maxSteerForce);
        return steer
    
    def separation(self, birds):
        posSum = VectorE3(0.0, 0.0, 0.0)
        repulse = VectorE3(0.0, 0.0, 0.0)
        for i in range(0, len(birds)):
            if random() > 0.6:
                pass
            else:
                bird = birds[i]
                distance = bird.position.distanceTo(self.position)
                if distance > 0 and distance <= self._neighborhoodRadius:
                    repulse = self.position - bird.position
                    repulse.normalize()
                    repulse.divideScalar(distance)
                    posSum.add(repulse)
        return posSum

def Borg():
    geometry = Geometry();
    vertices = geometry.vertices
    
    vertices.append(VectorE3( 5,  0,  0))
    vertices.append(VectorE3(-5, -2,  1))
    vertices.append(VectorE3(-5,  0,  0))
    vertices.append(VectorE3(-5, -2, -1))
    
    vertices.append(VectorE3( 0,  2, -6))
    vertices.append(VectorE3( 0,  2,  6))
    vertices.append(VectorE3( 2,  0,  0))
    vertices.append(VectorE3(-3,  0,  0))
    
    faces = geometry.faces
    faces.append(Face3(0, 2, 1))
    faces.append(Face3(4, 7, 6))
    faces.append(Face3(5, 6, 7))
    
    geometry.computeCentroids()
    geometry.computeFaceNormals()
    
    material = MeshBasicMaterial({"color": random() * 0xFFFFFF, "side": DoubleSide})
    return Mesh(geometry, material)

# Don't need to set the aspect for the camera - the workbench will do that.
camera = PerspectiveCamera(75.0, 1.0, 1.0, 10000.0)
camera.position.z = 450

scene = Scene()

renderer = CanvasRenderer()
renderer.setClearColor(Color(0xFFFFFF), 1.0)

workbench3D = Workbench3D(renderer.domElement, renderer, camera)

def escKey(event, downFlag):
    event.preventDefault()
    global timeOut
    timeOut = 0

keyHandlers = {
 27: escKey
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except:
        pass

birds = []
borgs = []
    
def setUp():
    for i in range(0, 10):
        bird = Bird()
        bird.setAvoidWalls(True)
        bird.setWorldSize(500, 500, 500)
        bird.phase = floor(random() * 62.83)
        birds.append(bird)
        
        borg = Borg()
        borg.position = bird.position
        borgs.append(borg)
        scene.add(borg)
        
    workbench3D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def render(t):
    for i in range(0, len(birds)):
        bird = birds[i]
        
        bird.run(birds)
        
        borg = borgs[i]
            
        color = borg.material.color
        c = (500.0 - bird.position.z) / 1000.0
        color.r = c
        color.g = c
        color.b = c
            
        borg.rotation.y = atan2(-bird.velocity.z, bird.velocity.x)
        borg.rotation.z = asin(-bird.velocity.y / bird.velocity.magnitude())

        bird.phase = (bird.phase + (max(0.0, borg.rotation.z) + 0.1)) % 62.83
        temp = sin(bird.phase) * 5
        borg.geometry.vertices[4].y = temp
        borg.geometry.vertices[5].y = temp
            
    renderer.render(scene, camera)

def terminate(t):
    return t > timeOut

def tearDown(e):
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()
    if e:
        print e

war = WindowAnimationRunner(render, terminate, setUp, tearDown, window)
war.start()
