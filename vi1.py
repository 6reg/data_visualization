"""
Image Visualization Project.
"""
from simpleimage import SimpleImage

GREEN = 127
BLUE = 127

CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 200
test_file = 'data-test.txt'

def main():
    canvas = SimpleImage.blank(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.show()
    with open(test_file) as f:
        #ignores first 2 lines of the file
        main_info = f.readlines()[2:]
        for i in range(len(main_info)):
            #iterates through the file and gets the value
            value = main_info[i]
            #passes the value and position value to the make_rect to draw a rectangle in the canvas
            make_rect(i + 1,value,CANVAS_WIDTH,CANVAS_HEIGHT,len(main_info))


# makes the rectangle
def make_rect(pos,value,width,height,l):
    rect_height = height
    rect_width = width / l #divides the total width of the canvas by the total number of values in the file
    for y in range((pos - 1) * rect_width, pos * rect_width): # if pos = 2 then starts from 100 and end at 200
        for x in range (rect_height):
            #gets the pixel from canvas and manipulates it
            pixel = canvas.get_pixel(x,y)
            pixel.green = GREEN
            pixel.blue = BLUE
            pixel.red = round(value * 255)



if __name__ == '__main__':
    main()
