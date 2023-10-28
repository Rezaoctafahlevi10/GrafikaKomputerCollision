import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 

play = False 

def drawtext(ch,xpos,ypos,r,g,b):
    color = [r,g,b]
    fontstyle = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line = 0
    glRasterPos(xpos,ypos)
    for i in ch : 
        if i=='/n':
            line +=1 
            glRasterPos(xpos,ypos*line)
        else :
            glutBitmapCharacter(fontstyle,ord(i))
def bg_text():
    glColor3f(100.0,100.0,100.0)
    glBegin(GL_QUADS)
    glVertex2f(285,230)
    glVertex2f(492,230)
    glVertex2f(495,280)
    glVertex2f(285,280)
    glEnd()
def start_game():
    glPushMatrix()
    glColor3b(36,200,127)
    glBegin(GL_QUADS)
    glVertex2f(280,220)
    glVertex2f(480,220)
    glVertex2f(480,280)
    glVertex2f(280,280)
    glEnd()
    glColor3ub(20,30,40)
    glBegin(GL_LINE_LOOP)
    glVertex2f(280,220)
    glVertex2f(480,220)
    glVertex2f(480,280)
    glVertex2f(280,280)
    glEnd()
    glScale(1,1,0)
    drawtext("PlayGame",320,250,25,0,0)
    glPopMatrix()
def ply_game():
    glPushMatrix()
    glBegin(GL_QUADS)
    glVertex2f(200,120)
    glVertex2f(300,120)
    glVertex2f(300,180)
    glVertex2f(280,180)
    glEnd()
    glPopMatrix()
def key_start (key,x,y):
    global play
    if ord(key) == ord (b'\r'): #keyboard function input keyboard
        play = True 
def play_game_mouse (button,state,x,y):
    global play
    if button == GLUT_RIGHT_BUTTON:
        if (x>=280 and x<= 480) and (y>=220 and y <=280):
            play = True
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    if play == True :
        ply_game()
    else : 
        start_game()
    glutSwapBuffers()
def init():
     glClearColor(0, 128, 128, 2.0)
     gluOrtho2D(0, 500.0, -500.0, 500.0)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 650,0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def Main():
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 500)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("Game")
    glutKeyboardFunc(key_start)
    glutMouseFunc(play_game_mouse)
    glutDisplayFunc(showScreen)
    init()
    glutIdleFunc(showScreen)
    glutMainLoop()
Main()