from browser import window

THREE = window.THREE

v = THREE.Vector3(1,2,3)
w = THREE.Vector3(0.5,0.5,0.5)

print v.x, v.y, v.z
# Unfortunately, THREE does not support toString.
print str(v)
print repr(v)

z = v + w
print z.x, z.y, z.z

z = v - w
print z.x, z.y, z.z
