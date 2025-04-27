from js import addCube, addSphere, setPosition

def cube(size):
    addCube(size)

def sphere(radius):
    addSphere(radius)

def translate(v):
    x, y, z = v
    setPosition(x, y, z)
