

def box(width, height):
    for x in range(width, height):
        print x

width = int(raw_input("width? "))
height = int(raw_input("height? "))

box(width, height)