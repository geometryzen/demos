# Here's a trigonometry problem that I encountered while tutoring a high school student:
#
# A person walks the following legs in order:
#
# 1) 100m east.
# 2) 300m south.
# 3) 150m on a bearing which is 30 degrees south of west.
# 4) 200m on a bearing which is 60 degrees north of west.
#
# What is the the total displacement of the person following the walk?
#
# While the student was accustomed to thinking of the displacements in terms of magnitudes
# and directions, the terminology of the questions and answers was to measure the directions
# using bearings. The student was just short of the stage in her career where she would start
# thinking in terms of basis vectors and coordinates. So the problem gets solved by identifying
# the "hidden" right triangles and applying trig formulae and Pythagoras' theorem.
#
# It got me wondering about the trajectory that we use to teach students. I'm a believer in the
# power of Geometric Algebra. But how should we introduce it? Thinking about this problem, I suggest
# that we can look at it using a framework that is a bit like a three-dimensional cube. We start from
# the lower-left-front corner as a beginner and want to proceed to the (opposite) upper-right-back
# corner where we have a high degree of mastery. Each direction in this cube represents a different
# aspect of complexity. The dimesions of complexity we have are:
# 1) Left to Right: Coordinate versus Vectoral and Geometric.
# 2) Down to Up: Number of dimensions of the Linear Space.
# 3) Front to Back: Metric (Flat to Curved, Euclidean through Lorentzian to curved spaces).
#
# My sense is that we hang out on the left plane of this cube with coordinate approaches, matrices
# and finally tensors. We do a lot of Linear algebra, S.R. with coordinates emphasizing transformations,
# and maybe touch quaternions for rotations.
# We start with 2 dimensional spaces and progress to 3 and 4+. This low-dimensional aspect makes sense, we have some intuition
# for two dimensions, can graph it easily, can play with complex numbers and matrix rotations.
#
# But this learning trajectory sacrifices the rewards of a more geometric approach that allows our intuition to be developed
# and offers greater opportunity for elegant computation using computers, freeing us to work on the more conceptual aspects.
#
# My conviction is that a better trajectory would be to develop a curriculum with the following trajectory:
#
# Start in the lower-left-ront corner them move to the right:
#
# 1a) Start with 2D, coordinates, Euclidean space.
# 1b) Move left-to-right in the cube to introduce vectors, Geometric Algebra, scalars and bivector.
# 1c) Relate the GA of the plane to complex numbers.
# 1d) Relate the GA of the plane to matrices.
# 1e) Develop ideas of Linear Transformations using the Geometric Algebra approach.
# 1f) Introduce theorems relating to Linear spaces on dimensionality, independence.
# 1g) Express Physics in 2D using GA: Reflections, Rotations, Circular Motion.
#
# Now move upwards in the cube to 3D:
#
# 2a) Explore double-sided rotations.
# 2b) Relationship to quaternions.
# 2c) Relationship to Pauli matrices.
# 2d) Physics includes Electrodynamics, magnetic field as a bivector.
# 2e) Alternatively, do Electrodynamics after S.R.
#
# Finally move towards the back starting with (flat) Lorentzian spaces.
#
# 3a) Special relativity. Geometric approach emphasizes invariants over transformations.
# 3b) S.R. connection with Electrodynamics. Develop latter from former?
# 3c) Introduce curved spaces for General Relativity.
# 3d) Conformal GA for Computer Graphics.
#
# So the example below will be a solution of the trig problem using GA to rotate some of the 
# vectors. We then just sum the vectors to get the total displacement.
from e2ga import *
from math import pi, sqrt, cos, sin

def showValue(name, m):
    print name + " => " + str(m)
    return m

# Create a few unit vectors to match the "compass" terminology in the question:
north = VectorE2(0, 1)
east = VectorE2(1, 0)
south = -north
west = -east

def toRadians(deg):
    return deg * pi / 180

# This is the most complex function that we must write.
def towards(a, b, theta):
    '''
    Returns a vector which is the result of rotating a towards b by and angle theta.
    '''
    denom = 2 * (1 + (b << a)).w
    print repr(denom)
    R = (1 + a * b) / sqrt(denom)
    print repr(R)
    return b

showValue("east towards south by 30 degrees", towards(east, south, toRadians(30)))
