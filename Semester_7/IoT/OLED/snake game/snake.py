from draw import Draw
import random, utime, _thread
from machine import Pin,PWM

class Snake:
    def __init__(self):
        self.buzzer=Pin(20,Pin.OUT)
        self.obj=Draw()
        self.head=(25,31)
        self.body=[(i,31) for i in range(self.head[0]-20,self.head[0]+1)] # head included
        self.border=[(i,0) for i in range(128)]+[(i,63) for i in range(128)]+[(0,i) for i in range(64)]+[(127,i) for i in range(64)]

    def intro(self):
        self.obj.clear()
        self.obj.oled.text("Game Starts",20,22)
        for i in range(5,0,-1):
            self.obj.oled.text(f"in {i} seconds",15,38)
            self.obj.show()
            self.obj.oled.text(f"in {i} seconds",15,38,0)
            utime.sleep(1)
        self.obj.clear()
        # borders
        for point in self.border:
            self.obj.point(*point)

    def render(self,food,visible=1):
        self.obj.glow=visible
        for point in self.body:
            self.obj.point(*point)
        self.obj.point(*self.head)
        self.obj.point(*food)

    def condtion(self):
        if self.head in self.border or self.head in self.body:
            return False
        return True
    
    def randomFood(self):
        while True:
            food=random.randrange(1,126),random.randrange(1,62)
            if not food in self.body:
                return food

    def move(self,direction,up,down,left,right):
        head=self.head
        if direction==up:
            return head[0],head[1]-1
        elif direction==down:
            return head[0],head[1]+1
        elif direction==left:
            return head[0]-1,head[1]
        elif direction==right:
            return head[0]+1,head[1]
        
    
    def play(self,up,down,left,right):
        def buzzerListner(pin,duration=0.3):
            pwm=PWM(pin)
            pwm.freq(10)
            def alarm():
                for i in range(1000,20001,500):
                    pwm.duty_u16(i)
                    utime.sleep(0.01)
                for i in range(20000,-1,-500):
                    pwm.duty_u16(i)
                    utime.sleep(0.01)
            if duration==3:
                alarm()
            else:
                pwm.duty_u16(5000)
                utime.sleep(0.1)
                pwm.duty_u16(0)
                # pin.value(1)
                # utime.sleep(duration)
                # pin.value(0)

        upBtn=Pin(up,mode=Pin.IN, pull=Pin.PULL_DOWN)
        downBtn=Pin(down,mode=Pin.IN,pull=Pin.PULL_DOWN)
        leftBtn=Pin(left,mode=Pin.IN,pull=Pin.PULL_DOWN)
        rightBtn=Pin(right,mode=Pin.IN,pull=Pin.PULL_DOWN)

        self.intro()        

        direction=right
        food=(80,31)
        self.render(food)
        self.obj.show()

        while True:
            if upBtn.value() and direction!=down:
                direction=up
            elif downBtn.value() and direction!=up:
                direction=down
            elif leftBtn.value() and direction!=right:
                direction=left
            elif rightBtn.value() and direction!=left:
                direction=right
            
            self.render(food,0)
            self.head=self.move(direction,up,down,left,right)
            if not self.condtion():
                _thread.start_new_thread(buzzerListner,(self.buzzer,3))
                break
            self.body.append(self.head)
            utime.sleep(.01)
            if self.head==food:
                _thread.start_new_thread(buzzerListner,(self.buzzer,0.5))
                food=self.randomFood()
            else:
                self.body.pop(0)
            self.render(food)
            self.obj.show()

        self.obj.clear()
        self.obj.oled.text("Game Over",20,22,0)
        self.obj.oled.text(f"Your Score:{len(self.body)-21}",10,38,0)
        self.obj.show()
        utime.sleep(5)

