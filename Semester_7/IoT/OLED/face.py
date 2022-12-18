from draw import Draw
import utime

class Face:

    def face():
        obj=Draw()
        obj.circle((64,32),20)  # head
        obj.circle((54,26),2)   # eye1
        obj.circle((74,26),2)   # eye2
        obj.triangle((64,28),(62,34),(66,34)) # nose
        obj.rectangle((60,40),(68,43))  # mouth
        obj.show()

    def liveFace():
        obj=Draw()
        def head():
            obj.circle((64,32),20)  # head
            obj.triangle((64,28),(62,34),(66,34))   # nose

        def eyeOpen(visible=1):
            obj.glow=visible
            obj.circle((54,26),2)   # eye1
            obj.circle((74,26),2)   # eye2

        def eyeClose(visible=1):
            obj.glow=visible
            obj.line((52,26),(56,26))
            obj.line((72,26),(76,26))

        def mouthOpen(visible=1):
            obj.glow=visible
            obj.rectangle((60,40),(68,43))
        def mouthClose(visible=1):
            obj.glow=visible
            obj.rectangle((60,42),(68,42))

        def talk(duration=0.5,times=1):
            obj.oled.text("Hi",0,0,1)
            for i in range(times):
                mouthOpen(0)
                mouthClose()
                obj.show()
                utime.sleep(duration)
                mouthClose(0)
                mouthOpen()
                obj.show()
                utime.sleep(duration)
            obj.oled.text("Hi",0,0,0)
                


        def blink(duration=0.5,times=1):
            for i in range(times):
                eyeOpen(0)
                eyeClose()
                obj.show()
                utime.sleep(duration)
                eyeClose(0)
                eyeOpen()
                obj.show()
                utime.sleep(duration)
            
        head()
        eyeOpen()
        mouthOpen()
        for i in range(5):
            blink(times=3)
            talk(times=2)