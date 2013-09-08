from three import *

projector = Projector();

def onDocumentMouseDown(event):
    # Convert window coordinates to normalized device coordinates.
    mouseVector = Vector3(2 * (event.clientX / canvasWidth) - 1, 1 - 2 * (event.clientY - canvasHeight)
    raycaster = projector.pickingRay(mouseVector.clone(), camera)
    intersects = raycaster.intersectObject(objects)
    if (intersects.length > 0):
        # intersects record includes object,face,faceIndex,distance,point
        intersects[0].object.material.color.setRGB(random(), random(), random())
        
        sphere = Mesh(sphereGeom, sphereMaterial)
        sphere.position = intersects[0].point
        scene.add(sphere)