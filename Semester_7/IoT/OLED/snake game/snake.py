from draw import Draw
import random, utime
from machine import Pin

class Snake:

    obj=Draw()
    obj.clear()
    head=(25,31)
    body=[(i,31) for i in range(head[0]-20,head[0]+1)] # head included
    border=[(i,0) for i in range(128)]+[(i,63) for i in range(128)]+[(0,i) for i in range(64)]+[(127,i) for i in range(64)]

    def intro():
        Snake.obj.oled.text("Game Starts",20,22)
        for i in range(5,0,-1):
            Snake.obj.oled.text(f"in {i} seconds",15,38)
            Snake.obj.show()
            Snake.obj.oled.text(f"in {i} seconds",15,38,0)
            utime.sleep(1)
        Snake.obj.clear()
        # borders
        for point in Snake.border:
            Snake.obj.point(*point)

    def render(food,visible=1):
        Snake.obj.glow=visible
        for point in Snake.body:
            Snake.obj.point(*point)
        Snake.obj.point(*Snake.head)
        Snake.obj.point(*food)

    def condtion():
        if Snake.head in Snake.border or Snake.head in Snake.body:
            return False
        return True
    
    def randomFood():
        while True:
            food=random.randrange(1,126),random.randrange(1,62)
            if not food in Snake.body:
                return food

    def move(direction,up,down,left,right):
        head=Snake.head
        if direction==up:
            return head[0],head[1]-1
        elif direction==down:
            return head[0],head[1]+1
        elif direction==left:
            return head[0]-1,head[1]
        elif direction==right:
            return head[0]+1,head[1]
        
    
    def play(up,down,left,right):
        upBtn=Pin(up,mode=Pin.IN, pull=Pin.PULL_DOWN)
        downBtn=Pin(down,mode=Pin.IN,pull=Pin.PULL_DOWN)
        leftBtn=Pin(left,mode=Pin.IN,pull=Pin.PULL_DOWN)
        rightBtn=Pin(right,mode=Pin.IN,pull=Pin.PULL_DOWN)

        Snake.intro()        

        direction=right
        food=(80,31)
        Snake.render(food)
        Snake.obj.show()

        while True:
            if upBtn.value() and direction!=down:
                direction=up
            elif downBtn.value() and direction!=up:
                direction=down
            elif leftBtn.value() and direction!=right:
                direction=left
            elif rightBtn.value() and direction!=left:
                direction=right
            
            Snake.render(food,0)
            Snake.head=Snake.move(direction,up,down,left,right)
            # utime.sleep(1)
            if not Snake.condtion(): 
                break
            Snake.body.append(Snake.head)
            utime.sleep(.01)
            if Snake.head==food:
                food=Snake.randomFood()
            else:
                Snake.body.pop(0)
            Snake.render(food)
            Snake.obj.show()

        Snake.obj.clear()
        Snake.obj.oled.text("Game Over",20,22,0)
        Snake.obj.oled.text(f"Your Score:{len(Snake.body)-21}",10,38,0)
        Snake.obj.show()
        utime.sleep(10)
