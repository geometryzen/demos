// This little trick (not to be copied!) is a temporary undocumented feature.
var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

log('Hello, World!!');

log(blade.UNIT_KILOGRAM.toString())
log(blade.UNIT_METER.toString())
log(blade.UNIT_SECOND.toString())
log(blade.UNIT_AMPERE.toString())
log(blade.UNIT_KELVIN.toString())
log(blade.UNIT_MOLE.toString())
log(blade.UNIT_CANDELA.toString())

var quantity = new blade.Euclidean3(1,0,0,0,0,0,0,0);

var unit = blade.UNIT_INCH;

var measure = new blade.Measure<blade.Euclidean3>(quantity, unit);

log(measure);

var sq = measure.mul(measure);

var q = sq.quantity;
var u = sq.uom;

log(sq);

log(u);
/*
print "The seven base SI units are..."
show("mass", kilogram)
show("length", meter)
show("time", second)
show("electric current", ampere)
show("thermodynamic temperature", kelvin)
show("amount of substance", mole)
show("luminous intensity", candela)
print
print "Some derived units are..."
show("electric charge", coulomb)
show("force", newton)
show("energy", joule)
show("power", watt)
# TODO: Use the formatting function.
print "electric potential " +str(volt)
print "magnetic flux density " +str(tesla)
print "electric field strength " +str(volt/meter)
print "resistance " +str(volt/ampere)
print "conductance " +str(ampere/volt)
print "permittivity " +str((coulomb ** 2)/(newton*(meter ** 2)))
print "permeability " +str(tesla * meter/ampere)
print "angular momentum " +str(joule * second)
print "frequency " +str(1 / second)
print "pressure, stress " +str(newton /(meter ** 2))
print "capacitance " +str(coulomb/volt)
print "magnetic flux " +str(volt * second)
print "inductance " +str(tesla * (meter ** 2)/ampere)
print "dynamic viscosity " +str(newton * second/meter **2)
print "moment of force " +str(newton * meter)
print "surface tension " +str(newton/meter)
print "heat flux density " +str(watt/meter ** 2)
print "heat capacity, entropy " +str(joule/kelvin)
print "thermal conductivity " +str(watt/(meter*kelvin))
print "energy density " +str(joule/(meter**3))
print "molar energy " +str(joule/mole)
print "molar entropy " +str(joule/(mole*kelvin))
*/