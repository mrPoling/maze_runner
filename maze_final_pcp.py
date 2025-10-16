################################################################################
#   a124TR_mazerunner2_move_runner.py
#   Example solution: 
#      The maze runner can now move about the maze.
################################################################################
import turtle as trtl
import random as rand

# maze configuration variables
num_sides = 23
path_width = 25 
wall_color = "blue"
stopped = False
wn = trtl.Screen()

def draw_door(pos):
  maze_drawer.forward(pos)
  maze_drawer.penup()
  maze_drawer.forward(path_width*2)
  maze_drawer.pendown()

def draw_barrier(pos):
  maze_drawer.forward(pos)
  maze_drawer.left(90)
  maze_drawer.forward(path_width*2)
  maze_drawer.backward(path_width*2)
  maze_drawer.right(90)

def move_runner():
  global stopped
  if (not stopped): maze_runner.forward(2)
  
  # determine if runner hits a wall
  wn_canvas = wn.getcanvas()
  x,y  = maze_runner.position()
  margin = 8
  
  # find_overlappting defines a rectangle returns a list of items drawn within that rectangle
  # Why -y? Just ignore that for now ;)
  items = wn_canvas.find_overlapping(x+margin, -y+margin, x-margin, -y-margin)
  
  if (len(items) > 0): # >2 items overlappig
    # get the fill color of the base object - the canvas
    canvas_color = wn_canvas.itemcget(items[0], "fill")
    
    #if the canvas is currently the wall color, the turtle has "collided"
    #or if the turtle is out of bounds, 
    if (canvas_color == wall_color) or (abs(x) + 20 > wn.window_width()/2 ) or (abs(y) + 20 > wn.window_height()/2 ):
      maze_runner.fillcolor("gray")
      stopped = True
      return
  # automatically move the runner
  wn.ontimer(move_runner, 30) # fires every X ms


def reset_maze_runner():
    global stopped
    stopped = False
    maze_runner.fillcolor("green")

# event handlers for changing direction
def go_up():
  maze_runner.setheading(90)
  reset_maze_runner()
def go_down():
  maze_runner.setheading(270)
  reset_maze_runner()
def go_left():
  maze_runner.setheading(180)
  reset_maze_runner()
def go_right():
  maze_runner.setheading(0)  
  reset_maze_runner()


# config the maze
maze_drawer = trtl.Turtle()
maze_drawer.pensize(5)
maze_drawer.pencolor(wall_color)
maze_drawer.speed("fastest")
maze_drawer.penup()
maze_drawer.goto(path_width*2, -path_width*2)
maze_drawer.pendown()

# config the maze runner
maze_runner = trtl.Turtle(shape="turtle")
maze_runner.fillcolor("green")
maze_runner.penup()
maze_runner.goto(-path_width*2, path_width*2)
maze_runner.pendown()

# draw maze from the middle out
wall_len = path_width
for w in range(num_sides): 
  wall_len += path_width

  if (w > 4): 
    maze_drawer.left(90)

    # randomize location of doors and barriers in wall
    door = rand.randint(path_width*2, (wall_len - path_width*2))
    barrier = rand.randint(path_width*2, (wall_len - path_width*2))
    # if a door and barrier would be rendered on top of each other, get a new value
    while abs(door - barrier) < path_width:
      door = rand.randint(path_width*2, (wall_len - path_width*2))

    if (door < barrier):
      draw_door(door)
      draw_barrier(barrier - door - path_width*2)
      # draw the rest of the wall
      maze_drawer.forward(wall_len - barrier)
    else: 
      draw_barrier(barrier)
      draw_door(door - barrier)
      # draw the rest of the wall
      maze_drawer.forward(wall_len - door - path_width*2)

maze_drawer.hideturtle()

# listen for events
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')
wn.onkeypress(move_runner, 'g')

wn.listen()

wn.mainloop()