from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random
import os 

#inisialisasi object 
collison_object_x = 100 
collison_object_y = 300
pos_x = 0
pos_y=0

def collison_object (): 
    global collison_object_x,collison_object_y
    glPushMatrix()
    glTranslated(collison_object_x,collison_object_y,0)
    glColor3f(200,55,55)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glVertex2f(10,0)
    glVertex2f(10,10)
    glVertex2f(0,10)
    glEnd()
    glPopMatrix()
def benda():
    global pos_x,pos_y,collison_object_x,collison_object_y
    glPushMatrix()

    glTranslated(pos_x,pos_y,0)
    # if (pos_x == collison_object_x and pos_y == collison_object_y):
    #     print('collision : ', pos_x , pos_y)
    if (pos_x < collison_object_x + 10 and pos_x+10 > collison_object_x 
        and pos_y < collison_object_y +5 and pos_y+5>collison_object_y ) :
             print('collision : ', pos_x , pos_y)
    glColor3f(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glVertex2f(10,0)
    glVertex2f(10,10)
    glVertex2f(0,10)
    glEnd()
    glPopMatrix()
def random_object (): 
    global collison_object_x,collison_object_y
    collison_object_x=random.randint(0,500)
    collison_object_y=random.randint(0,500)
def input_keyboard(key,x,y):
    global pos_x,pos_y
    os.system('cls')
    if key == GLUT_KEY_UP: 
        pos_y+=5
        print('Tombol up ditekan ', "x : ", pos_x , "y :" , pos_y )
    elif key == GLUT_KEY_DOWN : 
        pos_y-=5
        print('Tombol down ditekan ', "x : ", pos_x , "y :" , pos_y )
    elif key == GLUT_KEY_RIGHT:
        pos_x+=5 
        print('Tombol right ditekan ', "x : ", pos_x , "y :" , pos_y )
    elif key == GLUT_KEY_LEFT : 
        pos_x -= 5
        print('Tombol left ditekan ', "x : ", pos_x , "y :" , pos_y )
def key_keyboard (key,x,y):
    global pos_x,pos_y
    if ord(key) == ord ('a'):
         pos_y+=5
         print('Tombol up ditekan ', "x : ", pos_x , "y :" , pos_y )
    elif ord(key) == ord ('d'):
         pos_y-=5
         print('Tombol up ditekan ', "x : ", pos_x , "y :" , pos_y )
    elif ord(key) == ord ('w'):
         pos_x+=5
         print('Tombol up ditekan ', "x : ", pos_x , "y :" , pos_y )
    elif ord(key) == ord ('e'):
         pos_x-=5
         print('Tombol up ditekan ', "x : ", pos_x , "y :" , pos_y )
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    benda()
    collison_object()
    glutSwapBuffers()

def init():
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(0, 500.0, 0, 500.0)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def Main():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)  # Use GLUT_DOUBLE for double buffering
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("Game")
    glutDisplayFunc(showScreen)
    glutSpecialFunc(input_keyboard)
    glutKeyboardFunc(key_keyboard)
    init()
    random_object()
    glutIdleFunc(showScreen)
    glutMainLoop()

Main()
