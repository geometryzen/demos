from three import *

def onDocumentMouseDown(event):
    mouseVector = Vector3(2 * (event.clientX / canvasWidth) - 1, 1 - 2 * (event.clientY - canvasHeight)
    projector = Projector();
    raycaster = projector.pickingRay(mouseVector.clone(), camera)