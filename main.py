import colorgram
import turtle as t
import random


t.colormode(255)
colors = colorgram.extract('image.jpg', 10)
color_list = []

my_turtle = t.Turtle()
screen = t.Screen()
my_turtle.speed("fastest")


for i in range(8):
    current_color = colors[i]
    current_color = current_color.rgb  # Color is returned in rgb format in the form of named tuple
    r = current_color.r
    g = current_color.g
    b = current_color.b
    color_tuple = (r,g,b)

    color_list.append(color_tuple)

my_turtle.penup()
my_turtle.setheading(210)
my_turtle.forward(300)
my_turtle.setheading(0)
my_turtle.pendown()

total_dots = 100

for dot_count in range(1, total_dots + 1):
    my_turtle.dot(20 , random.choice(color_list))
    my_turtle.penup()
    my_turtle.forward(50)
    my_turtle.pendown()
    if dot_count % 10 == 0:         # Should be the number of dots in each row
        my_turtle.setheading(90)
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)        # This should be equal to the dots in each row * forward steps between 2 dots ( 10 * 50 )
        my_turtle.setheading(0)
        my_turtle.pendown()


# print(color_list)

screen.exitonclick()