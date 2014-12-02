from math import *
from browser import window

WIDTH = 400
HEIGHT = 400

class Color:
  def __init__(self, red, green, blue):
    self._red = red;
    self._green = green;
    self._blue = blue;

  def luminance(self):
    return Color.luminance(self._red, self._green, self._blue)
    
  def __str__():
    return "rgb(" + this._red + ", " + this._green + "," + this._blue + ")"

  def asFillStyle(self):
    return "rgb(" + str(floor(self._red*255)) + ", " + str(floor(self._green*255)) + "," + str(floor(self._blue*255)) + ")"

  def luminance(red, green, blue):
    gamma = 2.2
    return 0.2126 * pow(red, gamma) + 0.7152 * pow(green, gamma) + 0.0722 * pow(blue, gamma)

  def fromHSL(H, S, L):
    C = (1 - abs(2*L-1)) * S;
    def normalizeAngle(angle):
      if (angle > 2 * pi):
        return normalizeAngle(angle - 2 * pi)
      elif (angle < 0):
        return normalizeAngle(angle + 2 * pi)
      else:
        return angle

    def matchLightness(R, G, B):
      x = Color.luminance(R, G, B)
      m = L - (0.5 * C)
      return Color(R + m, G + m, B + m)
    
    sextant = ((normalizeAngle(H) / pi) * 3) % 6
    X = C * (1 - abs(sextant % 2 - 1))
    if (sextant >= 0 and sextant < 1):
      return matchLightness(C,X,0.0)
    elif (sextant >= 1 and sextant < 2):
      return matchLightness(X,C,0.0)
    elif (sextant >= 2 and sextant < 3):
      return matchLightness(0.0,C,C*(sextant-2))
    elif (sextant >= 3 and sextant < 4):
      return matchLightness(0.0,C*(4-sextant),C)
    elif (sextant >= 4 and sextant < 5):
      return matchLightness(X,0.0,C)
    elif (sextant >= 5 and sextant < 6):
      return matchLightness(C,0.0,X)
    else:
      return matchLightness(0.0,0.0,0.0)

class Canvas:
  def __init__(self, width, height):
    self._width = width;
    self._height = height;
    self.wnd = window.open("", "", "width=" + str(width) + ", height=" + str(height), False);
    
    popDoc = self.wnd.document
    
    canvas = popDoc.createElement("canvas")
    
    canvas.setAttribute("id", "graph")
    canvas.setAttribute("width",  str(width))
    canvas.setAttribute("height", str(height))
    
    popDoc.body.appendChild(canvas)
    popDoc.body.style.margin = "0"
    
    self.context = canvas.getContext("2d")
  
  def draw(self):
    self.context.fillStyle = self.backgroundColor.asFillStyle() 
    self.context.fillRect(0, 0, self._width, self._height);

  def close():
    this.wnd.close()

class Complex:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def mod(self):
    return sqrt(self.x * self.x + self.y * self.y)

  def arg(self):
    return atan2(self.y, self.x)

  def __add__(self, other):
    return Complex(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Complex(self.x - other.x, self.y - other.y)

  def __mul__(self, other):
    return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

  def __div__(self, other):
    denom = other.x * other.x + other.y * other.y;
    return Complex((self.x * other.x + self.y * other.y)/denom, (self.y * other.x - self.x * other.y)/denom)

  def __repr__(self):
    return "Complex(" + str(self.x) + ", " + str(self.y) + ")"

  def __str__(self):
    return str(self.x) + "+" + str(self.y) + "i"

def f(z):
  return z;
  #return new Complex(1,0).divide(z);
  '''
  var z3 = z.multiply(z).multiply(z);
  var z2 = z.multiply(z);
  var sz = new Complex(6,0).multiply(z);
  var tw = new Complex(20,0);
  return z3.add(z2).add(sz).subtract(tw);
  '''

class MinMax:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    def __str__(self):
        return "min: " + str(self.min) + ", max: " + str(self.max)

def sigmoid(t):
  return 1 / (1 + exp(-t*t/2000))

def lightnessFromMagnitude(r):
  return 2 * sigmoid(r) - 1.0

class ComplexPlane:
  def __init__(self, xRange, yRange, f):
    self.xRange = xRange
    self.yRange = yRange
    self.f = f
    self._canvas = Canvas(WIDTH, HEIGHT)

  def draw(self):
    for X in range(WIDTH):
      for Y in range(HEIGHT):
        x = (X / WIDTH) * (self.xRange.max - self.xRange.min) + self.xRange.min
        y = ((HEIGHT-Y)/HEIGHT) * (self.yRange.max - self.yRange.min) + self.yRange.min
        print x,y
        '''
        z = Complex(x,y)
        H = self.f(z).arg()
        S = 1
        L = lightnessFromMagnitude(self.f(z).mod())
        #L = 0.5
        self._canvas.context.fillStyle = Color.fromHSL(H, S, L).asFillStyle()
        self._canvas.context.fillRect(X,Y,1,1)
        '''

R = 10
canvas = Canvas(WIDTH, HEIGHT)
canvas.draw()
#cp = ComplexPlane(MinMax(-R,+R), MinMax(-R,+R),f)
#cp.draw()

