# PointLight.py
from three import *

light = PointLight(0xff0000, 1, 100)

print light
print str(light)
print repr(light)
print type(light)
print str(type(light))
print repr(type(light))
print "color:" + str(light.color)


