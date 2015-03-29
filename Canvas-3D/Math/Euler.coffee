# Euler.coffee
log = (s) -> Sk.output(s+'\n')

a = new THREE.Euler(0, 1, 1.57, 'XYZ')
b = new THREE.Vector3(1, 0, 1)
c = b.applyEuler(a)

log c.x
log c.y
log c.z