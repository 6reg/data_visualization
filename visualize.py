"""
Image Visualization Project.

This program creates visualizations of data sets that 
change over time. For example, 'child-mortality.txt' 
is loaded in and the output is a vsualization of the 
change in child mortality around the world from 1960 
until 2017. Red means high and green means low. 

"""
from simpleimage import SimpleImage

DATA_SET = 'data-illiteracy.txt'

GREEN = 127
BLUE = 127

MAX_RED_VALUE = 255

CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 200

def main():
    canvas = SimpleImage.blank(CANVAS_WIDTH, CANVAS_HEIGHT)   
    red_values = get_red_values()
    canvas = make_image(red_values, canvas)
    canvas.show()

def get_red_values():
    red_values = []
    with open(DATA_SET) as file:
        for i in range(2):
            next(file)
        for line in file:
            line = line.strip()
            red_values.append(round(float(line) * MAX_RED_VALUE))
    return red_values

def get_pixel_color(red_value, pixel):
    pixel.red = red_value
    pixel.green = GREEN
    pixel.blue = BLUE
    return pixel

def make_image(red_values, canvas):
    # Get width each stripe should be
    stripe_width = CANVAS_WIDTH // len(red_values) # 100 // 11 = 100
    # Create blank canvas as wide as length of data set
    new_canvas = SimpleImage.blank(stripe_width * len(red_values), CANVAS_HEIGHT)
    # For each stripe on canvas..
    for each_stripe in range(len(red_values)):
        for x in range(stripe_width):
            for y in range(CANVAS_HEIGHT):
                # Get starting point of each "each_stripe"
                start_x = stripe_width * each_stripe + x
                pixel = canvas.get_pixel(start_x, y)
                # Update pixel with red value from data set
                pixel = get_pixel_color(red_values[each_stripe], pixel)
                new_canvas.set_pixel(start_x, y, pixel)
    return new_canvas




if __name__ == '__main__':
    main()
