from draw import Draw
import utime


def face():
    obj=Draw()
    obj.circle((64,32),20)
    obj.circle((54,22),2)
    obj.circle((74,22),2)
    obj.rectangle((64,28),(65,34))
    obj.rectangle((60,40),(68,43))
    obj.show()
    pass

def style():
    obj=Draw()
    c=0
    while True:
        obj.line((0+c,10),(20+c,30))
        obj.line((0+c,50),(20+c,30))

        obj.line((127-c,10),(107-c,30))
        obj.line((127-c,50),(107-c,30))
        obj.show()
        # utime.sleep(0.25)
        obj.clear()
        c+=1
        if c>128 : break


face()
style()
face()

obj=Draw()
# obj.point(0,0)
# obj.point(127,63)   # 128*64
# # obj.rectangle((35,30),(65,0))
# obj.rectangleFill((12,12),(20,20))
# obj.circle((64,32),20)
# # obj.line((20,20),(50,60))
# # obj.line((50,60),(20,20))
# # obj.line((0,20),(0,50))
# # obj.line((40,10),(50,20))
# obj.triangle((0,0),(30,0),(30,30))

# obj.circleFill((64,32),15)

# obj.rectangleFill((35,30),(65,0))

# c=60
# while True:
#     # obj.line((0,c),(130,c))
#     obj.show()
#     obj.point(0,c)
#     print(c)
#     # obj.rectangle((c,c),(c+15,c+15))
#     c+=1
#     utime.sleep(1)
#     # obj.clear()
    

obj.show()
