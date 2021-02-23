# import colorgram
# all_colors = colorgram.extract('image.jpg',6)
# print(all_colors)

# # color_list = [<colorgram.py Color: Rgb(r=239, g=228, b=209), 33.79930860288896%>, <colorgram.py Color: Rgb(r=66, g=32, b=9), 15.179309301269889%>, <colorgram.py Color: Rgb(r=86, g=95, b=113), 13.33209176725292%>, <colorgram.py Color: Rgb(r=242, g=215, b=232), 13.025192151750414%>, <colorgram.py Color: Rgb(r=217, g=159, b=86), 12.645738518423677%>, <colorgram.py Color: Rgb(r=166, g=82, b=30), 12.018359658414132%>]
# rgb_colors = []

# for color in all_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


import turtle as turtle_module
import random 

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()


# choose a starting point
tim.setheading(255)
tim.forward(250)
tim.setheading(0)


color_list = [(239, 228, 209), (66, 32, 9), (86, 95, 113), (242, 215, 232), (217, 159, 86), (166, 82, 30)]
for dot_count in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()