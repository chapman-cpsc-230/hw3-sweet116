import turtle

# Ask user for input here.
t = turtle.Pen()
# Now create a graphics window.
sides = int(input('enter odd number greater than five'))

side_len = int(input('enter number'))

for i in range(sides):
    t.forward(side_.len)
    t.left(100 - 100/sides)
    t.forward(side_len)

# Put the rest of your code can go here

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
