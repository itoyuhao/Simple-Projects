"""
File: my_drawing.py
Name: Kevin Chen
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

window = GWindow(800, 600)
DELAY = 1200


def main():
    """
    This picture has been made into animation, repeating 2 times
    """
    n = 2
    while n > 0:
        background()
        pause(DELAY)
        bird_chima()
        pause(DELAY)
        bird_tangyuan()
        pause(DELAY)
        chima_dialog()
        pause(DELAY)
        tangyuan_reaction()
        pause(DELAY)
        bird_name()
        pause(DELAY)
        sign_name()
        pause(DELAY)
        n -= 1


def background():
    # Background: sky & wires
    sky = GRect(800, 600)
    sky.filled = True
    sky.fill_color = 'powderblue'
    sky.color = 'powderblue'
    window.add(sky)

    wire_1 = GRect(800, 2, x=0, y=345)
    wire_1.filled = True
    wire_1.fill_color = 'dimgray'
    wire_1.color = 'dimgray'
    window.add(wire_1)

    wire_2 = GRect(800, 2, x=0, y=350)
    wire_2.filled = True
    wire_2.fill_color = 'dimgray'
    wire_2.color = 'dimgray'
    window.add(wire_2)


def bird_chima():
    # Chima body
    body = GOval(100, 100, x=190, y=240)
    body.filled = True
    body.fill_color = 'olivedrab'
    body.color = 'olivedrab'
    window.add(body)

    # Chima head
    head = GOval(80, 80, x=200, y=200)
    head.filled = True
    head.fill_color = 'olivedrab'
    head.color = 'olivedrab'
    window.add(head)

    # Chima neck
    head = GArc(140, 140, 45, 90, x=190, y=248)
    head.filled = True
    head.fill_color = 'yellow'
    head.color = 'yellow'
    window.add(head)

    # Chima left eye white
    left_white_of_eye = GOval(20, 20, x=215, y=215)
    left_white_of_eye.filled = True
    left_white_of_eye.fill_color = 'ivory'
    left_white_of_eye.color = 'ivory'
    window.add(left_white_of_eye)

    # Chima right eye white
    right_white_of_eye = GOval(20, 20, x=245, y=215)
    right_white_of_eye.filled = True
    right_white_of_eye.fill_color = 'ivory'
    right_white_of_eye.color = 'ivory'
    window.add(right_white_of_eye)

    # Chima left eye gray
    left_gray_of_eye = GOval(15, 15, x=218, y=217)
    left_gray_of_eye.filled = True
    left_gray_of_eye.fill_color = 'gray'
    left_gray_of_eye.color = 'gray'
    window.add(left_gray_of_eye)

    # Chima right eye gray
    right_gray_of_eye = GOval(15, 15, x=248, y=217)
    right_gray_of_eye.filled = True
    right_gray_of_eye.fill_color = 'gray'
    right_gray_of_eye.color = 'gray'
    window.add(right_gray_of_eye)

    # Chima left eye black
    left_black_of_eye = GOval(10, 10, x=220, y=219)
    left_black_of_eye.filled = True
    left_black_of_eye.fill_color = 'black'
    left_black_of_eye.color = 'black'
    window.add(left_black_of_eye)

    # Chima right eye black
    right_black_of_eye = GOval(10, 10, x=250, y=219)
    right_black_of_eye.filled = True
    right_black_of_eye.fill_color = 'black'
    right_black_of_eye.color = 'black'
    window.add(right_black_of_eye)

    # Chima left eye reflect
    left_reflect_of_eye = GOval(3, 3, x=224, y=220)
    left_reflect_of_eye.filled = True
    left_reflect_of_eye.fill_color = 'gainsboro'
    left_reflect_of_eye.color = 'gainsboro'
    window.add(left_reflect_of_eye)

    # Chima right eye reflect
    right_reflect_of_eye = GOval(3, 3, x=252, y=220)
    right_reflect_of_eye.filled = True
    right_reflect_of_eye.fill_color = 'gainsboro'
    right_reflect_of_eye.color = 'gainsboro'
    window.add(right_reflect_of_eye)

    # Chima beak
    beak = GPolygon()
    beak.add_vertex((235, 240))
    beak.add_vertex((240, 252))
    beak.add_vertex((245, 240))
    beak.add_vertex((240, 237))
    beak.filled = True
    beak.fill_color = 'sienna'
    beak.color = 'sienna'
    window.add(beak)

    # Chima left claw
    claw1 = GLine(x0=210, y0=330, x1=200, y1=345)
    claw2 = GLine(x0=210, y0=330, x1=210, y1=350)
    claw3 = GLine(x0=210, y0=330, x1=220, y1=345)
    window.add(claw1)
    window.add(claw2)
    window.add(claw3)

    # Chima right claw
    claw4 = GLine(x0=270, y0=330, x1=260, y1=345)
    claw5 = GLine(x0=270, y0=330, x1=270, y1=350)
    claw6 = GLine(x0=270, y0=330, x1=280, y1=345)
    window.add(claw4)
    window.add(claw5)
    window.add(claw6)


def bird_tangyuan():
    # Tangyuan body
    body = GOval(130, 100, x=420, y=240)
    body.filled = True
    body.fill_color = 'whitesmoke'
    body.color = 'whitesmoke'
    window.add(body)

    # Tangyuan head
    head = GOval(90, 90, x=440, y=180)
    head.filled = True
    head.fill_color = 'whitesmoke'
    head.color = 'whitesmoke'
    window.add(head)

    # Tangyuan left eye black
    left_black_of_eye = GOval(6, 6, x=450, y=215)
    left_black_of_eye.filled = True
    left_black_of_eye.fill_color = 'black'
    left_black_of_eye.color = 'black'
    window.add(left_black_of_eye)

    # Tangyuan right eye black
    right_black_of_eye = GOval(6, 6, x=480, y=215)
    right_black_of_eye.filled = True
    right_black_of_eye.fill_color = 'black'
    right_black_of_eye.color = 'black'
    window.add(right_black_of_eye)

    # Tangyuan beak
    beak = GPolygon()
    beak.add_vertex((430, 240))
    beak.add_vertex((460, 230))
    beak.add_vertex((465, 237))
    beak.add_vertex((460, 245))
    beak.filled = True
    beak.fill_color = 'firebrick'
    beak.color = 'firebrick'
    window.add(beak)

    # Tangyuan left claw
    claw1 = GLine(x0=445, y0=330, x1=435, y1=345)
    claw2 = GLine(x0=445, y0=330, x1=445, y1=350)
    claw3 = GLine(x0=445, y0=330, x1=455, y1=345)
    window.add(claw1)
    window.add(claw2)
    window.add(claw3)

    # Tangyuan right claw
    claw4 = GLine(x0=525, y0=330, x1=515, y1=345)
    claw5 = GLine(x0=525, y0=330, x1=525, y1=350)
    claw6 = GLine(x0=525, y0=330, x1=535, y1=345)
    window.add(claw4)
    window.add(claw5)
    window.add(claw6)


def chima_dialog():
    # Word_cloud_1
    cloud = GRect(120, 60, x=175, y=100)
    cloud.filled = True
    cloud.fill_color = 'white'
    cloud.color = 'white'
    window.add(cloud)

    # Word_cloud_2
    cloud = GOval(60, 60, x=150, y=100)
    cloud.filled = True
    cloud.fill_color = 'white'
    cloud.color = 'white'
    window.add(cloud)

    # Word_cloud_3
    cloud = GOval(60, 60, x=270, y=100)
    cloud.filled = True
    cloud.fill_color = 'white'
    cloud.color = 'white'
    window.add(cloud)

    # Word_cloud_4
    cloud = GPolygon()
    cloud.add_vertex((230, 160))
    cloud.add_vertex((270, 160))
    cloud.add_vertex((240, 180))
    cloud.filled = True
    cloud.fill_color = 'white'
    cloud.color = 'white'
    window.add(cloud)

    # Content
    text = GLabel('Who r u?')
    text.color = 'tomato'
    text.font = 'Courier-15-bold'
    window.add(text, x=192, y=143)


def tangyuan_reaction():
    # Question mark
    text = GLabel('?')
    text.color = 'tomato'
    text.font = 'Courier-30-italic-bold'
    window.add(text, x=515, y=195)


def bird_name():
    # chima
    text = GLabel('芝麻')
    text.color = 'lightseagreen'
    text.font = 'Courier-20-bold'
    window.add(text, x=210, y=400)

    # tanyuan
    text = GLabel('湯圓')
    text.color = 'darkgrey'
    text.font = 'Courier-20-bold'
    window.add(text, x=450, y=400)


def sign_name():
    sign = GLabel('Kevin 2021.03.13')
    sign.color = 'steelblue'
    sign.font = 'Courier-10-bold'
    window.add(sign, x=665, y=600)







if __name__ == '__main__':
    main()
