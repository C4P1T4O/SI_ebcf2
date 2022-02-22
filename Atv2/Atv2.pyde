
import random 
from Food import Food
from Vehicle import Vehicle

def setup():
    global v
    global food
    global x
    global y
    size(872, 600)
    textSize(30)
    velocity = PVector(0, 0)
    vel = PVector(0, 0)
    v = Vehicle(width / 2, height / 2, velocity)
    x = random.randint(1, 871)
    y = random.randint(1, 599)
    food = Food(x, y, vel)


def draw():
    
    background(255,215,0)
    atacar = PVector(food.position.x, food.position.y)
    food.update()
    food.display()
    contador = int(0)
    text(u"Comida: ",50, 50)
    text(food.contado,180, 50)
    if ((food.fPosition().dist(v.vPosition()) > 1)):
        v.arrive(atacar)
    else:
        velocity = PVector(0, 0)
        v.velocity = velocity
        food.contado = food.contado + 1
        contador = food.contado
        print (contador)
        x = random.randint(1, 871)
        y = random.randint(1, 599)
        food.position = PVector(x, y)
        food.update()
        food.display()
    v.update()
    v.display()
    
    
