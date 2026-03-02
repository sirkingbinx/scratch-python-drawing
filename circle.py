# Circle drawing
# NOTE: comments are not implemented; omit them when importing

pen.color(0, 0, 255) # blue
move(0, -50) # initial point

pen.down()

repeat 360:
    transform.rotation.add(1) # change angle by one
    transform.position.step(1) # move 1 step

pen.up() # we done