from draw import Draw
from machine import Pin
import utime

class LisNav:
    obj=Draw()
    index=0
    games=[]
    btn_bounce_t1=0

    def setGames(games):
        LisNav.games=games

    def render():
        LisNav.obj.clear()
        items=LisNav.items
        row=0
        for i in range(len(items)):
            if LisNav.index==i:
                LisNav.obj.rectangleFill((0,row-2),(100,row+8))
                LisNav.obj.text(items[i],0,row,0)
            else:
                LisNav.obj.text(items[i],0,row,1)
            row+=10

    def buttonListener(pin):
        btn_bounce_t2=utime.ticks_ms()
        if btn_bounce_t2-LisNav.btn_bounce_t1>1000:
            LisNav.btn_bounce_t1=btn_bounce_t2
            if pin==LisNav.btnDown:
                LisNav.index=(LisNav.index+1)%len(LisNav.items)
            elif pin==LisNav.btnUp:
                LisNav.index=(LisNav.index-1)%len(LisNav.items)
            elif pin==LisNav.btnOk:
                LisNav.dropAllButtons()
                LisNav.startGame()
            LisNav.render()
            LisNav.obj.show()
    
    def dropAllButtons():
        LisNav.btnUp.irq(handler=None)
        LisNav.btnDown.irq(handler=None)
        LisNav.btnOk.irq(handler=None)

    def navigate(items,x=17,y=16,z=15):
        LisNav.items=items
        LisNav.render()
        LisNav.obj.show()

        LisNav.btnUp=Pin(x,Pin.IN,pull=Pin.PULL_DOWN)
        LisNav.btnDown=Pin(y,Pin.IN,pull=Pin.PULL_DOWN)
        LisNav.btnOk=Pin(z,Pin.IN,pull=Pin.PULL_DOWN)

        LisNav.btnUp.irq(LisNav.buttonListener,trigger=Pin.IRQ_RISING)
        LisNav.btnDown.irq(LisNav.buttonListener,trigger=Pin.IRQ_RISING)
        LisNav.btnOk.irq(LisNav.buttonListener,trigger=Pin.IRQ_RISING)

    def startGame():
        LisNav.games[LisNav.index]().play(17,16,18,19)
        LisNav.navigate(LisNav.items)
    

