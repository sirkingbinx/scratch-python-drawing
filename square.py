# Square drawing
# NOTE: comments are not implemented; omit them when importing

pen.color(0, 0, 0) # pen color in RGB (0 - 255)
move(-10, -10) # initial point

pen.down() # now we are drawing

move(10, -10)
move(10, 10)
move(-10, 10)
move(-10, 10)

pen.up() # end drawing here