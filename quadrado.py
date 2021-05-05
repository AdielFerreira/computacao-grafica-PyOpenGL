
from OpenGL.GL import *
from OpenGL.GLUT import *


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.00, 0.00, 0.0)
    glVertex3f(0.75, 0.00, 0.0)
    glVertex3f(2.0, 2.0, 0.0)
    glVertex3f(0.00, 0.75, 0.0)
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(350, 350)
glutInitWindowPosition(100, 100)
wind = glutCreateWindow("hello")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(display)
glutMainLoop()
