from js import addCube, addSphere, addCylinder, setPosition, setRotation, setScale, setColor, union, difference, intersection

def cube(size):
    addCube(size)

def sphere(radius):
    addSphere(radius)

def cylinder(h, r):
    addCylinder(r, h)

def translate(v):
    x, y, z = v
    setPosition(x, y, z)

def rotate(v):
    x, y, z = v
    setRotation(x, y, z)

def scale(v):
    x, y, z = v
    setScale(x, y, z)

def color(rgb):
    r, g, b = rgb
    setColor(r/255, g/255, b/255)

def union_():
    union()

def difference_():
    difference()

def intersection_():
    intersection()
