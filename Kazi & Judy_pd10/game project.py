#J.K.Game Company
#Cart Rider
#car,road...
#We want other objects to come towards the car and the player has to dodge it.
#Problems and Chalenges:background stopped moving 
from gamelib import *

game = Game(800, 600,"Game")



bk = Animation("images\\roadsprite.png",100,game,8000/10,8000/10,1)
game.setBackground(bk)

car = Image("images\\car.png",game)
car.resizeBy(5)
car.moveTo(300,700)

car.setSpeed(1,180)

boulder = Image("images\\boulder.png",game)
banana = Image("images\\banana.png",game)
banana =[]
zoom = Sound("car.wav",1)
splat = Sound("banana.wav",2)
for times in range(10):
    banana.append(Image("images\\banana.png",game))
for b in banana:
    b.resizeBy(-70)
    b.setSpeed(1,180)
    b.moveTo(randint(10,750),randint(-800,-50))
    
while not game.over:
    game.processInput()
    game.drawBackground()
    game.displayScore()

    for b in banana:
        b.move()
        
    car.move()
    if keys.Pressed[K_UP]:
        zoom.play()
        car.y-=5
        car.resizeBy(-1)

    if keys.Pressed[K_LEFT]:
        zoom.play()
        car.x-=3
        

    if keys.Pressed[K_RIGHT]:
        zoom.play()
        car.x+=3
        
                    
    for b in banana:
        b.move()
        b.y+=2
        b.resizeBy(-1)
        if b.isOffScreen("bottom"):
            b.moveTo(randint(10,750),randint(-800,-50))
            b.resizeTo(863,558)
            b.move()
            b.y+=2

        if car.collidedWith(b,"rectangle"):
            splat.play()
            b.visible = False
            b.moveTo(randint(10,750),randint(-800,-50))
            b.resizeTo(863,558)
            b.visible = True

           
            
    if car.width<=10 and car.height<=10:
                
        car.resizeTo(800,600)
        car.moveTo(300,700)


        
                
        

    


    game.update(60)
game.quit()


