# PoyhedraSubdivision.py
from math import *
	 
"""Construct an eight-sided polyhedron"""
f = sqrt(2.0) / 2.0

verts = [
    ( 0, -1,  0),
	(-f,  0,  f),
	( f,  0,  f),
	( f,  0, -f),
	(-f,  0, -f),
	( 0,  1,  0) ]

faces = [
    (0, 2, 1),
    (0, 3, 2),
    (0, 4, 3),
    (0, 1, 4),
    (5, 1, 2),
    (5, 2, 3),
    (5, 3, 4),
    (5, 4, 1) ]

def subdivide(verts, faces):
    """Subdivide each triangle into four triangles, pushing verts to the unit sphere"""
    triangles = len(faces)
    print triangles
    for faceIndex in range(triangles):
        print faceIndex
        # Create three new verts at the midpoints of each edge:
        face = faces[faceIndex]
        print face
        for vertIndex in face:
            print vertIndex
            print verts[vertIndex]
        print ((verts[vertIndex]) for vertIndex in face)    
        a,b,c = (Vector3(*verts[vertIndex]) for vertIndex in face)
        verts.append((a + b).normalized()[:])
        verts.append((b + c).normalized()[:])
        verts.append((a + c).normalized()[:])

        # Split the current triangle into four smaller triangles:
        i = len(verts) - 3
        j, k = i+1, i+2
        faces.append((i, j, k))
        faces.append((face[0], i, k))
        faces.append((i, face[1], j))
        faces[faceIndex] = (k, j, face[2])

    return verts, faces

print subdivide(verts, faces)