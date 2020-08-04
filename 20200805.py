import turtle

# Create 4 dictionaries of different turtle specifications to use as values in the turtles dictionary
turtle1 = {'color': 'red', 'pensize': 1, 'fillcolor': 'yellow', 'squaresize': 50, 'x': 50, 'y': 100}
turtle2 = {'color': 'blue', 'pensize': 5, 'fillcolor': 'red', 'squaresize': 100, 'x': 300, 'y': 150}
turtle3 = {'color': 'green', 'pensize': 7, 'fillcolor': 'blue', 'squaresize': 150, 'x': 50, 'y': 400}
turtle4 = {'color': 'yellow', 'pensize': 10, 'fillcolor': 'green', 'squaresize': 200, 'x': 250, 'y': 450}

# Create 4 turtle objects to use as the keys in the turtles dictionary
todd = turtle.Turtle()
tina = turtle.Turtle()
tyrell = turtle.Turtle()
talisha = turtle.Turtle()

# Make the turtles dictionary by associating each turtle object with a set of specs
turtles = {todd: turtle1, tina: turtle2, tyrell: turtle3, talisha: turtle4}

# Turtle maker function sets up the turtle passed in with correct color, size, fill etc. from specs passed in
def turtle_maker(turtle, specs):
  turtle.color(specs['color'])
  turtle.pensize(specs['pensize'])
  turtle.fillcolor(specs['fillcolor'])
  turtle.penup()

# Draw square function sends turtle to its coords then draws and fills the correct sized square
def draw_square(turtle, size, x, y):
  turtle.goto(x, y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)
  turtle.end_fill()

# Main program loop, loops through turtles in the dictionary, creates turtle then draws its square
for turtle, specs in turtles.items():
  turtle_maker(turtle, specs)
  draw_square(turtle, specs['squaresize'], specs['x'], specs['y'])
