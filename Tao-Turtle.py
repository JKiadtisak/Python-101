Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.screen.bgcolor("black")
tao.speed(30)

for i in range(60) :
    tao.pencolor("white")
    tao.circle(3*i)
    tao.circle(-3*i)
    tao.left(15)

    
tao.clear()
###############
for i in range (50) :
    tao.pencolor("yellow")
    tao.circle(2*i)
    tao.circle(-2*i)
    tao.right(10)

    
tao.clear()

########
for i in range (50) :
    tao.pencolor("green")
    tao.circle(2*i)
    tao.right(15)

    
tao.clear()
############
for i in range (60) :
    tao.pencolor("blue") 
    tao.circle(3*i)
    tao.circle(-3*i)
    tao.right(10)

    
for i in range (60) :
   tao.pencolor('yellow')
    tao.circle(3*i)
    tao.circle(-3*i)
    tao.right(10)
    
SyntaxError: unexpected indent

for i in range (60) :
    tao.pencolor("yellow")
    tao.circle(3*i)
    tao.circle(-3*i)
    tao.right(10)
... 
...     
>>> for i in range (60) :
...     tao.pencolor("yellow")
...     tao.circle(3*i)
...     tao.circle(-3*i)
...     tao.right(10)
... 
...     
>>> for i in range (60) :
...     tao.pencolor("Green")
...     tao.circle(3*i)
...     tao.circle(-3*i)
...     tao.right(10)
... 
...     
>>> tao.clear()
>>> ##########################
>>> for i in range (50) :
...     tao.pencolor("blue") 
...     tao.circle(2*i)
...     tao.right(15)
... 
...     
>>> for i in range (60) :
...    tao.pencolor("yellow")
...     tao.circle(3*i)
...     tao.circle(-3*i)
...     tao.right(10)
...     
SyntaxError: unexpected indent
>>> 
>>> for i in range (60) :
...     tao.pencolor("yellow")
...     tao.circle(3*i)
...     tao.circle(-3*i)
...     tao.right(10)
... 
...     
