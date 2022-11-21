import machine
import utime
import urandom

led = machine.Pin(1, machine.Pin.OUT) 
Lbutton = machine. Pin(16, machine.Pin.IN)
Rbutton = machine. Pin(17, machine.Pin.IN)

def button_press(pin):
    Lbutton.irq(handler=None)
    Rbutton.irq(handler=None)
    rection_time = utime.ticks_diff(utime.ticks_ms(), timer_light_off) 
    if pin==Lbutton:
        print('Left Player Won')
    else:
        print('Right Player Won')
    print("Your reaction time was " + str(rection_time) + " milliseconds!")

led.value(1)
utime.sleep(urandom.uniform (1,2))
led.value(0)
timer_light_off = utime.ticks_ms()
Lbutton.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press)
Rbutton.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press)

