var a = new THREE.Euler( 0, 1, 1.57, 'XYZ' );
var b = new THREE.Vector3( 1, 0, 1 );
var c = b.applyEuler(a);

console.log(c + "\n")