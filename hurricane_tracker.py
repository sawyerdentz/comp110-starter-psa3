"""
Module: hurricane_tracker

Program to visualize the path of a Hurrican in the North Atlantic Basin.

Authors:
1) Sawyer Dentz - sdentz@sandiego.edu
2) Matthew Oderlin - moderlin@sandiego.edu
"""
import turtle


def screen_setup():
    """
    Creates the Turtle and the Screen with the map background
    and coordinate system set to match latitude and longitude.

    Returns:
    A list containing the turtle, the screen, and the background image.

    DO NOT MODIFY THIS FUNCTION IN ANY WAY!!!
    """

    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Tracker")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()

    # set the coordinate system to match lat/long
    turtle.setworldcoordinates(-90, 0, -17.66, 45)

    map_bg_img = tkinter.PhotoImage(file="atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("hurricane.gif")
    t.shape("hurricane.gif")

    return [t, wn, map_bg_img]


# Define the get_category function here

def animate(csv_filename):
    """
    Animates the path of a hurricane.

    Parameters:
    csv_filename (string): Name of file containing hurricane data (CSV format).
    """

    # screen_setup returns a list of three items: the turtle to draw with, the
    # screen object for the window, and the background image of the window.
    # We only care about the turtle though.
    setup_data = screen_setup()

    # Give a name to the turtle that we were given back.
    hurricane_turtle = setup_data[0]


    # Your code to perform the animation will go after this line.
    f = open(csv_filename, "r")

    first_line = f.readline().split(",")
    hurricane_turtle.penup()
    hurricane_turtle.hideturtle()
    hurricane_turtle.goto(float(first_line[3]), float(first_line[2]))
    hurricane_turtle.pendown()
    hurricane_turtle.showturtle()
    
    if get_category(int(first_line[4])) == 1:
        hurricane_turtle.pencolor("blue")
        hurricane_turtle.pensize(2)
    elif get_category(int(first_line[4])) == 2:
        hurricane_turtle.pencolor("green")
        hurricane_turtle.pensize(3)
    elif get_category(int(first_line[4])) == 3:
        hurricane_turtle.pencolor("yellow")
        hurricane_turtle.pensize(4)
    elif get_category(int(first_line[4])) == 4:
        hurricane_turtle.pencolor("orange")
        hurricane_turtle.pensize(5)
    elif get_category(int(first_line[4])) == 5:
        hurricane_turtle.pencolor("red")
        hurricane_turtle.pensize(6)
    else:
        hurricane_turtle.pencolor("white")
        hurricane_turtle.pensize(1)

    for line in f:
        val = line.split(",")
        xval = float(val[3])
        yval = float(val[2])

        if get_category(int(val[4])) == 1:
            hurricane_turtle.pencolor("blue")
            hurricane_turtle.pensize(2)
        elif get_category(int(val[4])) == 2:
            hurricane_turtle.pencolor("green")
            hurricane_turtle.pensize(3)
        elif get_category(int(val[4])) == 3:
            hurricane_turtle.pencolor("yellow")
            hurricane_turtle.pensize(4)
        elif get_category(int(val[4])) == 4:
            hurricane_turtle.pencolor("orange")
            hurricane_turtle.pensize(5)
        elif get_category(int(val[4])) == 5:
            hurricane_turtle.pencolor("red")
            hurricane_turtle.pensize(6)
        else:
            hurricane_turtle.pencolor("white")
            hurricane_turtle.pensize(1)

        hurricane_turtle.goto(xval, yval)
        hurricane_turtle.write(get_category(int(val[4])))
    f.close()


    # DO NOT MODIFY THE FOLLOWING LINE! (It make sure the turtle window stays
    # open).
    turtle.done()

def get_category(wind_speed):

    """
    takes in a wind_speed parameter and returns the category that the hurricane is

    wind_speed: an integer of the hurricanes wind speed

    returns: an integer of the category that the hurricane is
    """

    if wind_speed >= 74 and wind_speed <= 95:
        return 1
    elif wind_speed >= 96 and wind_speed <= 110:
        return 2
    elif wind_speed >= 111 and wind_speed <= 129:
        return 3
    elif wind_speed >= 130 and wind_speed <= 156:
        return 4
    elif wind_speed > 156:
        return 5
    else:
        return 0
    

# Do not modify anything after this point.
if __name__ == "__main__":
    filename = input("Enter the name of the hurricane data file: ")
    animate(filename)
