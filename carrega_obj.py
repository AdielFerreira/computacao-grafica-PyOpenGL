from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pywavefront
from pywavefront import visualization

#pacotes necessarios para executar
#pip install pywavefront
#pip install pyglet

T = 0
T2 = 0
T3 = 0

quadric = None

def display():
    global quadric
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glRotatef(T ,0,0,1)
    glRotatef(T2,0,1,0)
    glRotatef(T3,1,0,0)
    
    visualization.draw(objeto)
    
    #gluCylinder(quadric,0.5,0.5,0.2,32,16);	
    #glutWireCube(0.5)
    #glutWireSphere(0.5, 36, 16)
    
    glPopMatrix()
    
    glutSwapBuffers()
    
def Keys(key, x, y):
    global T
    global T2
    global T3
    
    if(key == GLUT_KEY_LEFT ): 
        T -= 5 
    elif(key == GLUT_KEY_RIGHT ): 
        T += 5 
    elif(key == GLUT_KEY_UP ): 
        T2 -= 5 
    elif(key == GLUT_KEY_DOWN ): 
        T2 += 5 
    elif(key == GLUT_KEY_PAGE_UP ): 
        T3 += 5 
    elif(key == GLUT_KEY_PAGE_DOWN ): 
        T3 += 5         
       
def animacao(value):
    glutPostRedisplay()
    glutTimerFunc(30, animacao,1)
  

def init():
    global quadric
    glClearColor (0.3, 0.3, 0.3, 0.0)
    glShadeModel( GL_SMOOTH )
    glClearColor( 0.0, 0.0, 0.0, 0.0 )
    glClearDepth( 1.0 )
    glEnable( GL_DEPTH_TEST )
    glDepthFunc( GL_LEQUAL )
    glHint( GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST )

    glLightModelfv( GL_LIGHT_MODEL_AMBIENT, [0.3, 0.3, 0.3, 1.0] )
    glLightfv( GL_LIGHT0, GL_AMBIENT, [ 0.3, 0.3, 0.3, 1.0] )
    glLightfv( GL_LIGHT0, GL_DIFFUSE, [0.6, 0.6, 0.6, 1] )
    glLightfv( GL_LIGHT0, GL_POSITION, [2.0, 2.0, 1.0, 0.0])
    glEnable( GL_LIGHT0 )
    glEnable( GL_COLOR_MATERIAL )
    glShadeModel( GL_SMOOTH )
    glLightModeli( GL_LIGHT_MODEL_TWO_SIDE, GL_FALSE )
    glDepthFunc( GL_LEQUAL )
    glEnable( GL_DEPTH_TEST )
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
   
    #quadric=gluNewQuadric()								
    #gluQuadricNormals(quadric, GLU_SMOOTH)				
    #gluQuadricTexture(quadric, GL_TRUE)

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
wind = glutCreateWindow("Cubo")
init()
objeto = pywavefront.Wavefront('cubo.obj')
glutDisplayFunc(display)
glutTimerFunc(30,animacao,1)
glutSpecialFunc(Keys)
glutMainLoop()
