def triangle(height):
    for row in range(1, height + 1):
        spaces = height - row
        print " " * spaces + "*" * (row * 2 - 1)

height = int(raw_input("height? "))
base = height * 2 - 1

triangle(height)



def square(length, width):
    for number in range(length):
        print "*" * width

length = int(raw_input("length? "))
width = int(raw_input("width? "))

square(length, width)



def make_box(size):       
    for i in range(size):
        if i == 0 or i == size - 1:
            print("*"*(size+2))
        else:
            print("*" + " "*size + "*")

size = int(input('Please enter a positive integer between 1 and 15: '))

make_box(size)


