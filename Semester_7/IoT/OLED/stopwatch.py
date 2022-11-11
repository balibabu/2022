import time
class StopWatch:
    def start():
        StopWatch.startTime=time.time()
    def stop():
        StopWatch.endTime=time.time()
    def duration():
        return StopWatch.endTime-StopWatch.startTime
    